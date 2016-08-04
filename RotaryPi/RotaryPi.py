#!pirot_venv/bin/python

import RPi.GPIO as GPIO

class RotaryReaderConfig():
    def __init__(self, gpio):
        #BCM notation
        self.NUMBER_INPUT = 17
        self.NUMBER_OUTPUT = 27 
        self.DIALING_INPUT = 20 
        self.DIALING_OUTPUT = 21
        self.gpio = gpio

    def configure_gpio(self):
        self.gpio.setmode(GPIO.BCM)

        #Setup Number Pulse Encoder IO
        self.gpio.setup(self.NUMBER_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.gpio.setup(self.NUMBER_OUTPUT, GPIO.OUT)
        self.gpio.output(self.NUMBER_OUTPUT, True)

        #Setup Dialing Encoder IO
        self.gpio.setup(self.DIALING_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.gpio.setup(self.DIALING_OUTPUT, GPIO.OUT)
        self.gpio.output(self.DIALING_OUTPUT, True)


if __name__ == '__main__':
    '''Both dialing and number encoders are active low'''
    r = RotaryReaderConfig(GPIO)
    r.configure_gpio()
    print("**READING GPIO**")
    previous_number = 0
    current_number = 0
    previous_dialing =  0
    current_dialing = 0
    while True:
        current_number = GPIO.input(r.NUMBER_INPUT)
        current_dialing = GPIO.input(r.DIALING_INPUT)
        if(current_dialing != previous_dialing):
            if(current_dialing == 0):
                print("dialing ended")
            else:
                print("dialing now")

        previous_number = current_number
        previous_dialing = current_dialing







