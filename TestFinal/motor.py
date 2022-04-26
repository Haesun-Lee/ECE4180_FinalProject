import RPi.GPIO as GPIO # Allows us to interface with the GPIO pins

class Motor:
    # sets 2GPIO pins for clockwise and counter clockwise 
    def __init__(self, F, B):
        self.pinFwd = F
        self.pinBwd = B

        GPIO.setmode(GPIO.BOARD) # Sets the pins to use the Board Numbering

        GPIO.setup(self.pinFwd, GPIO.OUT) # Sets pin 1
        GPIO.setup(self.pinBwd, GPIO.OUT) # Sets pin 2

    def __del__(self):
        # Destructor cleans up any open pins
        GPIO.cleanup() 

    def forward(self):
        # Sets pin 1 to ON and pin 2 to OFF

        GPIO.output(self.pinFwd, GPIO.HIGH)
        GPIO.output(self.pinBwd, GPIO.LOW)

    def backward(self):
        # Sets pin 1 to OFF and pin 2 to ON

        GPIO.output(self.pinFwd, GPIO.LOW)
        GPIO.output(self.Bwd, GPIO.HIGH)

    def stop(self):
        # Sets both pins to OFF

        GPIO.output(self.pinFwd, GPIO.LOW)
        GPIO.output(self.pinBwd, GPIO.LOW)
