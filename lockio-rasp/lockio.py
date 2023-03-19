from gpiozero import LED


class Lockio:

    def __init__(self, id, localId, size, status, blockId, redGPIOPin, greenGPIOPin):
        self.id = id
        self.blockId = blockId
        self.localId = localId
        self.size = size
        self.status = status

        self.redGPIOPin = redGPIOPin
        self.greenGPIOPin = greenGPIOPin

        # only needed when testing remotely (when the server is not on raspberry)
        self.greenLED = LED(greenGPIOPin)
        self.redLED = LED(redGPIOPin)

    def updateLed(self):
        if self.status == "AVAILABLE":
            self.switchOn(self.greenLED)
            self.switchOff(self.redLED)
        elif self.status == "OCCUPIED":
            self.switchOn(self.redLED)
            self.switchOff(self.greenLED)
        elif self.status == "PRERESERVED":
            self.switchOn(self.redLED)
            self.switchOn(self.greenLED)
        else:
            self.switchOffAll()

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
