from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lockio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    local_id = db.Column(db.Integer)
    size = db.Column(db.String(20))
    status = db.Column(db.String(20))
    block_id = db.Column(db.Integer, db.ForeignKey('block.id'))



    def __init__(self, id, local_id, size, status, block_id):
        self.id = id
        self.block_id = block_id
        self.local_id = local_id
        self.size = size
        self.status = status

    @staticmethod
    def serialize(obj):
        if isinstance(obj, Lockio):
            return {
                'id': obj.id,
                'block_id': obj.block_id,
                'local_id': obj.local_id,
                'size': obj.size,
                'status': obj.status,
            }
        return obj

    # def switchOn(self, led):
    #     if led == self.green:
    #         self.green = True
    #     elif led == self.red:
    #         self.red = True
    #
    # def switchOff(self, led):
    #     if led == self.green:
    #         self.green = False
    #     elif led == self.red:
    #         self.red = False
    #
    # def switchOnAll(self):
    #     self.switchOn(self.green)
    #     self.switchOn(self.red)
    #
    # def switchOffAll(self):
    #     self.switchOff(self.green)
    #     self.switchOff(self.red)