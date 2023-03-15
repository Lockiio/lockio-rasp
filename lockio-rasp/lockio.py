from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from const.const import RASPBERRY_IP

class Lockio:

    def __init__(self, id, localId, size, status, blockId, redGPIOPin, greenGPIOPin):
        self.id = id
        self.blockId = blockId
        self.localId = localId
        self.size = size
        self.status = status

        # only needed when testing remotely (when the server is not on raspberry)
        raspberry = PiGPIOFactory(host=RASPBERRY_IP)
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