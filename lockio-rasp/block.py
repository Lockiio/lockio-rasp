from flask_sqlalchemy import SQLAlchemy
from lockio import Lockio

db = SQLAlchemy()

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lockio_id = db.Column(db.Integer, db.ForeignKey('lockio.id'))

    def __init__(self, id):
        self.id = id
        self.lockios = []

    def addLockio(self, lockio: Lockio):
        self.lockios.append(lockio)

    def addLockios(self, lockers):
        for lockio in lockers:
            self.addLockio(lockio)

    # def switchOnAll(self, color):
    #     if color == "green":
    #         for lockio in self.lockios:
    #             lockio.switchOn(lockio.green)
    #     elif color == "red":
    #         for lockio in self.lockios:
    #             lockio.switchOn(lockio.red)
    #
    # def switchOffAll(self, color):
    #     if color == "green":
    #         for lockio in self.lockios:
    #             lockio.switchOff(lockio.green)
    #     elif color == "red":
    #         for lockio in self.lockios:
    #             lockio.switchOff(lockio.red)

    def getLockio(self, id: int):
        for lockio in self.lockios:
            if lockio.id == id:
                return lockio
        raise ValueError("Pas de lockio avec id=" + str(id) + " existant");

    def getLockios(self):
        return self.lockios
