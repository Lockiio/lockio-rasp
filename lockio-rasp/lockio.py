from locker import Locker


class Lockio:

    def __init__(self, id):
        self.id = id
        self.lockers = []

    def addLocker(self, locker: Locker):
        self.lockers.append(locker)

    def addLockers(self, lockers):
        for locker in lockers:
            self.lockers.append(locker)

    def switchOnAll(self, color):
        if color == "green":
            for locker in self.lockers:
                locker.switchOn(locker.greenLED)
        elif color == "red":
            for locker in self.lockers:
                locker.switchOn(locker.redLED)

    def switchOffAll(self, color):
        if color == "green":
            for locker in self.lockers:
                locker.switchOff(locker.greenLED)
        elif color == "red":
            for locker in self.lockers:
                locker.switchOff(locker.redLED)