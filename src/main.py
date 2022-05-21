import asyncio
import sys
import keyboard

import server
from misc import configurator, navigation, logger


async def main():
    await server.controller.run_pump(1)  # TODO: Delete after test


if __name__ == "__main__":
    # Show menu
    logger.write("Server run")
    navigation.welcome_nav(menu_lvl=1)
    keyboard.add_hotkey("alt+s", server.controller.set_power_on)
    keyboard.add_hotkey("alt+d", server.controller.set_power_off)
    keyboard.add_hotkey("alt+e", configurator.run_configurator)

    # if sys.argv[0] is not None and sys.argv[0] == "--debug":
    #     print("\n~~~DEBUG OPTIONS~~~\n"
    #           "[Alt+Shift+F] Arduino firmware update")
    keyboard.add_hotkey("alt+shift+f", configurator.frimware_update)

    # Async awaiting server
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    # Check to exit
    while True:
        key = keyboard.read_key()
        if key == "esc":
            logger.write("Server down")

            break

    # Shutdown pump and close application

    server.controller.set_power_off()
    navigation.shutdown_application()
