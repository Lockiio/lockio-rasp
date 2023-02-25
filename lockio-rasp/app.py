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
    block_id = 1
    lockio1 = Lockio(1, 1, "SMALL", "OCCUPIED", block_id)
    lockio2 = Lockio(2, 2, "SMALL", "AVAILABLE", block_id)
    lockio3 = Lockio(3, 3, "MEDIUM", "AVAILABLE", block_id)
    lockio4 = Lockio(4, 4, "MEDIUM", "AVAILABLE", block_id)
    lockio5 = Lockio(5, 5, "MEDIUM", "OCCUPIED", block_id)
    lockio6 = Lockio(6, 6, "MEDIUM", "OCCUPIED", block_id)
    lockio7 = Lockio(7, 7, "LARGE", "DISABLED", block_id)
    lockio8 = Lockio(8, 8, "LARGE", "DISABLED", block_id)
    block = Block(block_id)
    block.addLockios([lockio1, lockio2, lockio3, lockio4, lockio5, lockio6, lockio7, lockio8])
    # Get the status of all lockios from the server
    response = requests.get(const.BACK_URL + "api/lockio/1/")

    # Uncomment the line below and comment the line above
    # to use the docker url on the N blocks from our Docker image
    # response = requests.get(const.DOCKER_URL + "api/lockio/1/")

    # TODO GET INFO FOR EACH LOCKIOS AND LIGHT THE LEDS WITH THEIR CORRECT STATUS
    print(response.json())

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
    status = request.json['status']
    if lockio.status == 'AVAILABLE':
        lockio.status = status
    return jsonify(vars(lockio)), 200


# GET all Lockios
@app.route(route, methods=['GET'])
def getAllLockios():
    lockios = block.getLockios()
    lockios_json = []
    for lockio in lockios:
        lockios_json.append(vars(lockio))
    return lockios_json, 200
