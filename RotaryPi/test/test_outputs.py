import unittest
from unittest.mock import MagicMock


import RotaryPi.RotaryPi as RotaryPi

class test_GPIO(unittest.TestCase):
    def test_configure_gpio(self):
        RotaryPi.configure_gpio()
