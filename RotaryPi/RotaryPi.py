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
        GPIO.wait_for_edge(r.DIALING_INPUT, GPIO.RISING)
        print("dialing now")
        number_pulse_count = 0
        while(GPIO.input(r.DIALING_INPUT) == True):
            current_number = GPIO.input(r.NUMBER_INPUT)
            if((current_number != previous_number) and (current_number==1)):
                print("number incremented")
                number_pulse_count += 1

            previous_number = current_number

        print("dialing ended, number was: {0}".format(number_pulse_count))

    
