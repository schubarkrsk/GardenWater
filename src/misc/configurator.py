import subprocess
from firmware import arduino
from misc import logger


def run_configurator():
    print("CONFIGURATOR")


def frimware_update():
    print("ARDUINO FIRMWARE UPDATE")
    logger.write("FIRMWARE UPDATE RUN", style="DEBUG")
    try:
        subprocess.check_call(arduino.flasher_call, shell=True)
    except:
        logger.write(Exception.with_traceback(), "ERROR")


if __name__ == "__main__":
    run_configurator()
