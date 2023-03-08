import requests
import const.const as const
from flask import *
from lockio import Lockio
from block import Block
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://dev:password@localhost/lockio"
db = SQLAlchemy(app)



def run():
    app.run()


# Use to run function at start of flask server
with app.app_context():

    lockios= db.session.query(Lockio).filter(Lockio.block_id == 1)
    #block_data=db.session.query(Block).filter(id == 1)
    block=Block(1)
    for lockio in lockios:
        lockio_instance = Lockio(
            id=lockio.id,
            block_id=lockio.block_id,
            local_id=lockio.local_id,
            size=lockio.size,
            status=lockio.status
        )
        block.addLockio(lockio_instance)

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
    return jsonify(Lockio.serialize(block.getLockio(lockio_id))), 200


# PATCH status of a Lockio
@app.route(route + '<int:lockio_id>', methods=['PATCH'])
def patchLockio(lockio_id):
    lockio = block.getLockio(lockio_id)
    lockio.status = request.json['status']
    return jsonify(Lockio.serialize(lockio)), 200


# GET all Lockios
@app.route(route, methods=['GET'])
def getAllLockios():
    lockios = block.getLockios()
    lockios_json = []
    for lockio in lockios:
        lockios_json.append(Lockio.serialize(lockio))
    return lockios_json, 200
