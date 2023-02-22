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
    lockio1 = Lockio(1, block_id, 1, "SMALL", "OCCUPIED")
    lockio2 = Lockio(2, block_id, 2, "SMALL", "AVAILABLE")
    lockio3 = Lockio(3, block_id, 3, "MEDIUM", "AVAILABLE")
    lockio4 = Lockio(4, block_id, 4, "MEDIUM", "AVAILABLE")
    lockio5 = Lockio(5, block_id, 5, "MEDIUM", "OCCUPIED")
    lockio6 = Lockio(6, block_id, 6, "MEDIUM", "OCCUPIED")
    lockio7 = Lockio(7, block_id, 7, "LARGE", "DISABLED")
    lockio8 = Lockio(8, block_id, 8, "LARGE", "DISABLED")
    block = Block(block_id)
    block.addLockios([lockio1, lockio2, lockio3, lockio4, lockio5, lockio6, lockio7, lockio8])
    # Get the status of all lockios from the server
    response = requests.get(const.BACK_URL + "api/lockio/1/")

    # TODO GET INFO FOR EACH LOCKIOS AND LIGHT THE LEDS WITH THEIR CORRECT STATUS
    print(response.json())

if __name__ == '__main__':
    run()

########
# ROUTES
########
route = "/api/rasp/1/lockios/"


@app.route(route + '<int:lockio_id>')
def get_Lockio(lockio_id):
    return jsonify(vars(block.getLockio(lockio_id))), 200


@app.route(route + '<int:lockio_id>', methods=['PATCH'])
def patch_Lockio(lockio_id):
    lockio = block.getLockio(lockio_id)
    status = request.json['status']
    if lockio.status == 'AVAILABLE':
        lockio.status = status
    return jsonify(vars(lockio)), 200


@app.route(route, methods=['GET'])
def get_Lockios():
    lockios = block.getLockios()
    lockios_json = []
    for lockio in lockios:
        lockios_json.append(vars(lockio))
    return lockios_json, 200
