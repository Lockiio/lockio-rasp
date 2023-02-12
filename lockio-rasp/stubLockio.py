
class stubLockio:

    mapLockio = {}
    def __init__(self, id : int, status : str):
        self.id=id;
        self.status=status;
        stubLockio.mapLockio[id]=self;

    def getListeLockio(self):
        return stubLockio.mapLockio;

    @staticmethod
    def getLockio(id :int):
        if id in stubLockio.mapLockio:
            return (stubLockio.mapLockio[id])
        else:
            raise ValueError("pas de lockio avec id="+id +" existant");

 
