#!pirot_venv/bin/python

import RPi.GPIO as GPIO


def configure_gpio(gpio):
    GPIO_INPUT = 6 #BCM notation
    GPIO_OUTPUT = 7 #BCM notation
    gpio.setmode(GPIO.BCM)
    gpio.setup(GPIO_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    gpio.setup(GPIO_OUTPUT, GPIO.OUT)

if __name__ == '__main__':
    configure_gpio(GPIO)
    print("HELLO FROM ROTARY PI")
