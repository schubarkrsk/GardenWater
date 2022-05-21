import asyncio

tasks = []


def set_power_on():
    print("Water pump is on")
    return None


def set_power_off():
    print("Water pump is down")
    return None


async def run_pump(run_time: float):
    set_power_on()
    await asyncio.sleep(run_time)
    set_power_off()
    return None
