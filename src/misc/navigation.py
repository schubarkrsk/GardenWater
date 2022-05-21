import sys
import keyboard


def welcome_nav(menu_lvl):
    if menu_lvl == 1:
        print("WELCOME TO GARDEN WATER APPLICATION\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "[Alt+S] Force power up pump\n"
              "[Alt+D] Force power down pump\n"
              "[Alt+E] Go to configurator mode\n"
              "[ESC] Shutdown server and shell-ui\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def shutdown_application():
    print("Goodbye! Press RETURN to close shell")
    keyboard.wait("return")
    sys.exit()
