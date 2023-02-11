from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


class Locker:

    def __init__(self, id, redGPIOPin, greenGPIOPin):
        # only needed when testing remotely (when the server is not on raspberry)
        raspberry = PiGPIOFactory(host='192.168.1.64')

        self.id = id
        self.greenLED = LED(greenGPIOPin, pin_factory=raspberry)
        self.redLED = LED(redGPIOPin, pin_factory=raspberry)

    def switchOnGreen(self):
        self.greenLED.on()

    def switchOffGreen(self):
        self.greenLED.off()

    def switchOnRed(self):
        self.redLED.on()

    def switchOffRed(self):
        self.redLED.off()

    def switchOff(self):
        self.switchOffGreen()
        self.switchOffRed()
