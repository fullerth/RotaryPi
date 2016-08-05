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
    #Define ports
    P_CTRL = 17
    P_INTR = 19

    def __init__(self):
        # Set the device class to a keyboard and set the name
        os.system("hciconfig hci0 class 0x002540")
        os.system("hciconfig hci0 name RotaryPi")
        # Make device discoverable
        os.system("hciconfig hci0 piscan")

        # Define server sockets for communication
        self.scontrol = BluetoothSocket(L2CAP)
        self.sinterrupt = BluetoothSocket(L2CAP)

        # Bind the sockets to a port
        self.scontrol.bind(("", Bluetooth.P_CTRL))
        self.sinterrupt.bind(("", Bluetooth.P_INTR))

if __name__=='__main__':
    b = Bluetooth()
