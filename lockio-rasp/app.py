import requests
import const.const as const
from flask import *
from lockio import Lockio
from block import Block

app = Flask(__name__, instance_relative_config=True)


def run():
    app.run()


# Use to run function at start of flask server
with app.app_context():
    # INIT BLOCK AND LOCKIOS
    block_id=1
    data_block=requests.get(const.BACK_URL+"api/lockio/1/blocks/"+str(block_id)).json()
    data_lockio=requests.get(const.BACK_URL+"api/lockio/1/blocks/"+str(block_id)+"/lockios/local").json()
    block= Block(data_block['id'])
    lockios = []

    for item in data_lockio:
        lockio = Lockio(item["id"],  item["localId"],item["size"], item["status"],block_id)
        lockios.append(lockio)

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
    return jsonify(vars(block.getLockio(lockio_id))), 200


# PATCH status of a Lockio
@app.route(route + '<int:lockio_id>', methods=['PATCH'])
def patchLockio(lockio_id):
    lockio = block.getLockio(lockio_id)
    lockio.status = request.json['status']
    return jsonify(vars(lockio)), 200


# GET all Lockios
@app.route(route, methods=['GET'])
def getAllLockios():
    lockios = block.getLockios()
    lockios_json = []
    for lockio in lockios:
        lockios_json.append(vars(lockio))
    return lockios_json, 200
