

class Lockio:
    mapLockio = {}
    listeLockio=[]

    def __init__(self, id,block_id,local_id,size,status):
        self.id = id;
        self.status = status;
        self.block_id=block_id;
        self.local_id=local_id;
        self.size = size
        self.status = status
        Lockio.mapLockio[id] = self;
        Lockio.listeLockio.append(self);


    @staticmethod
    def getListeLockio():
        return Lockio.listeLockio;

    @staticmethod
    def getLockio(id: int):
        if id in Lockio.mapLockio:
            return (Lockio.mapLockio[id])
        else:
            raise ValueError("pas de lockio avec id=" + id + " existant");


