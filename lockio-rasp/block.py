from lockio import Lockio

class Block:

    def __init__(self, id):
        self.id = id
        self.lockios = []

    def addLockio(self, lockio: Lockio):
        self.lockios.append(lockio)

    def addLockios(self, lockers):
        for lockio in lockers:
            self.addLockio(lockio)

    def switchOnAll(self, color):
        if color == "green":
            for lockio in self.lockios:
                lockio.switchOn(lockio.green)
        elif color == "red":
            for lockio in self.lockios:
                lockio.switchOn(lockio.red)

    def switchOffAll(self, color):
        if color == "green":
            for lockio in self.lockios:
                lockio.switchOff(lockio.green)
        elif color == "red":
            for lockio in self.lockios:
                lockio.switchOff(lockio.red)