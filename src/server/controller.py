import asyncio
from misc import logger

tasks = []


def set_power_on():
    logger.write("PUMP run")
    print("Water pump is on")
    return None


def set_power_off():
    logger.write("PUMP down")
    print("Water pump is down")
    return None


async def run_pump(run_time: float):
    logger.write(f"PUMP task on {run_time/60} minutes")
    set_power_on()
    await asyncio.sleep(run_time)
    set_power_off()
    return None
