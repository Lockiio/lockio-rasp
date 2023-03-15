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
                lockio.switchOn(lockio.greenLED)
        elif color == "red":
            for lockio in self.lockios:
                lockio.switchOn(lockio.redLED)

    def switchOffAll(self, color):
        if color == "green":
            for lockio in self.lockios:
                lockio.switchOff(lockio.greenLED)
        elif color == "red":
            for lockio in self.lockios:
                lockio.switchOff(lockio.redLED)


    def getLockio(self, id: int):
        for lockio in self.lockios:
            if lockio.id == id:
                return lockio
        raise ValueError("Pas de lockio avec id=" + str(id) + " existant");

    def getLockios(self):
        return self.lockios
