import unittest
from unittest.mock import MagicMock

import RPi.GPIO as GPIO

import RotaryPi.RotaryPi as RotaryPi

class test_GPIO(unittest.TestCase):
    def test_configure_gpio(self):
        mockGPIO = MagicMock()
        RotaryPi.configure_gpio(mockGPIO)
        mockGPIO.setup.assert_called_with(2, self.GPIO.OUT)
        mockGPIO.setup.assert_called_with(3, self.GPIO.IN, self.GPIO.PUD_DOWN)
