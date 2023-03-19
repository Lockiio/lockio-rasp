import requests
import const.const as const
from flask import *
from lockio import Lockio
from block import Block

app = Flask(__name__, static_folder='dist', static_url_path='/')


def run():
    app.run()


# Use to run function at start of flask server
with app.app_context():
    # INIT BLOCK AND LOCKIOS
    block_id = 1
    data_block = requests.get(const.DOCKER_URL + "api/lockio/1/blocks/" + str(block_id)).json()
    data_lockio = requests.get(const.DOCKER_URL + "api/lockio/1/blocks/" + str(block_id) + "/lockios/local").json()
    block = Block(data_block['id'])
    lockios = []

    for item in data_lockio:
        lockio = Lockio(item["id"], item["localId"], item["size"], item["status"], block_id, item["redGPIOPin"],
                        item["greenGPIOPin"])
        lockios.append(lockio)
        lockio.updateLed()

    block.addLockios(lockios)

if __name__ == '__main__':
    run()

########
# ROUTES
########
route = "/api/rasp/1/lockios/"


# GET unique Lockio
@app.route(route + '<int:lockio_id>')
def getLockio(lockio_id):
    lockio = block.getLockio(lockio_id)
    lockio_json = {"id": str(lockio.id), "localId": str(lockio.localId), "size": str(lockio.size),
                   "status": str(lockio.status)}
    return lockio_json, 200


# PATCH status of a Lockio
@app.route(route + '<int:lockio_id>', methods=['PATCH'])
def patchLockio(lockio_id):
    lockio = block.getLockio(lockio_id)
    lockio.status = request.json['status']
    lockio_json = {"id": str(lockio.id), "localId": str(lockio.localId), "size": str(lockio.size),
                   "status": str(lockio.status)}
    lockio.updateLed()
    return lockio_json, 200


# GET all Lockios
@app.route(route, methods=['GET'])
def getAllLockios():
    lockios = block.getLockios()
    lockios_json = []
    for lockio in lockios:
        lockio_json = {"id": str(lockio.id), "localId": str(lockio.localId), "size": str(lockio.size),
                       "status": str(lockio.status)}
        lockios_json.append(lockio_json)
    return lockios_json, 200


@app.route('/')
def index():
    return app.send_static_file('index.html')
