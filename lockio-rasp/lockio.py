class Lockio:

    def __init__(self,id,block_id,local_id,size,status):
        self.id = id
        self.status = status
        self.block_id = block_id
        self.local_id = local_id
        self.size = size
        self.status = status

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