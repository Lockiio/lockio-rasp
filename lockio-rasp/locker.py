from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


class Locker:

    def __init__(self, id, redGPIOPin, greenGPIOPin):
        # only needed when testing remotely (when the server is not on raspberry)
        raspberry = PiGPIOFactory(host='192.168.1.64')

        self.id = id
        self.greenLED = LED(greenGPIOPin, pin_factory=raspberry)
        self.redLED = LED(redGPIOPin, pin_factory=raspberry)

    def switchOn(self, led):
        if led == self.greenLED:
            self.greenLED.on()
        elif led == self.redLED:
            self.redLED.on()

    def switchOff(self, led):
        if led == self.greenLED:
            self.greenLED.off()
        elif led == self.redLED:
            self.redLED.off()

    def switchOnAll(self):
        self.switchOn(self.greenLED)
        self.switchOn(self.redLED)

    def switchOffAll(self):
        self.switchOff(self.greenLED)
        self.switchOff(self.redLED)