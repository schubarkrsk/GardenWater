# https://gist.github.com/ks156/87bfb4f07bf6682e1835
# All rights reserved to ks156
# Based as part opensource project

# !/usr/bin/python

import serial
import subprocess
import sys
import time

if len(sys.argv) != 3:
    print("Missing arguments")
    print("Usage :")
    print("   python flash_arduino.py path_to_fw path_to_serial")
    print("Example :")
    print("   python flash_arduino.py /root/myFirmware.hex /dev/ttyACM0")
    sys.exit()
# Args
fw = sys.argv[1]
port = sys.argv[2]

# Activate bootloader
try:
    ser = serial.Serial(port, baudrate=1200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS)
except:
    print("Serial port not available")
    sys.exit(1)

# Test if port is opened
try:
    ser.isOpen()
except:
    print("Serial port is not opened")
    sys.exit(2)

ser.close()

# At this point, the bootloader should be activated.

# Wait two second for the bootloader to be ready
time.sleep(2)

# Bootload
try:
    avrdude = "avrdude -patmega32u4 -cavr109 -P" + port + " -b57600 -Uflash:w:" + fw + ":a -C/etc/avrdude.conf"
    print(avrdude)
    subprocess.check_call(avrdude, shell=True)
except:
    print("Exception")
    sys.exit(3)

sys.exit()
