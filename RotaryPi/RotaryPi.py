#!pirot_venv/bin/python

import RPi.GPIO as GPIO

class RotaryReaderConfig():
    def __init__(self, gpio):
        self.GPIO_INPUT = 17 #BCM notation
        self.GPIO_OUTPUT = 27 #BCM notation
        self.gpio = gpio

    def configure_gpio(self):
        self.gpio.setmode(GPIO.BCM)
        self.gpio.setup(self.GPIO_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.gpio.setup(self.GPIO_OUTPUT, GPIO.OUT)
        self.gpio.output(self.GPIO_OUTPUT, True)

if __name__ == '__main__':
    r = RotaryReaderConfig(GPIO)
    r.configure_gpio()
    print("**READING GPIO**")
    previous_state = 0
    current_state = 0
    print("initial_state: {0}".format(previous_state))
    while True:
        current_state = GPIO.input(r.GPIO_INPUT)
        if(current_state != previous_state):
            print("current_state: {0}, previous_state: {1}".format(
                current_state, previous_state))
        previous_state = current_state







