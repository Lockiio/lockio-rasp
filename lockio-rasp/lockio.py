class Lockio:

    def __init__(self, id):
        self.id = id
        self.green = False
        self.red = False

    def switchOn(self, led):
        if led == self.green:
            self.green = True
        elif led == self.red:
            self.red = True

    def switchOff(self, led):
        if led == self.green:
            self.green = False
        elif led == self.red:
            self.red = False

    def switchOnAll(self):
        self.switchOn(self.green)
        self.switchOn(self.red)

    def switchOffAll(self):
        self.switchOff(self.green)
        self.switchOff(self.red)

    def getLockioInfo(self):
        print("Lockio " + self.id + " status: green = " + str(self.green) + " red = " + str(self.red))