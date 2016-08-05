import os
import sys
import bluetooth
from bluetooth import *
import dbus
import time
import evdev
from evdev import *
import keymap

class Bluetooth:
    def __init__(self):
        # Set the device class to a keyboard and set the name
        os.system("hciconfig hci0 class 0x002540")
        os.system("hciconfig hci0 name RotaryPi")
        # Make device discoverable
        os.system("hciconfig hci0 piscan")

if __name__=='__main__':
    b = Bluetooth()
