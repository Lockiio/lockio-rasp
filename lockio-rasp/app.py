import requests
import const.const as const
from flask import Flask, render_template, jsonify
from manage_leds import *
from stubLockio import LockioCase
app = Flask(__name__, instance_relative_config=True)


def run():
    app.run(host='0.0.0.0',debug=True)


# Use to run function at start of flask server
with app.app_context():

    # Get the status of all lockios from the server
    def getLockiosStatus():
        response = requests.get(const.BACK_URL + "api/lockio/1/")
        return response.json()

    # TODO GET INFO FOR EACH LOCKIOS AND LIGHT THE LEDS WITH THEIR CORRECT STATUS
    print(getLockiosStatus())
    ledsOn()

if __name__ == '__main__':
    run()


########
# ROUTES
########
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/rasp/1/led/on')
def enableLeds():
    ledsOn()
    return "Leds on"


@app.route('/api/rasp/1/led/off')
def disableLeds():
    ledsOff()
    return "Leds off"





block_id= 1;
lockio1 = LockioCase(1, block_id, 1, "SMALL","OCCUPIED")
lockio2 = LockioCase(2, block_id, 2,"SMALL", "AVAILABLE")
lockio3 = LockioCase(3, block_id, 3, "MEDIUM", "AVAILABLE")
lockio4 = LockioCase(4, block_id, 4, "MEDIUM", "AVAILABLE")
lockio5 = LockioCase(5, block_id, 5, "MEDIUM", "OCCUPIED")
lockio6 = LockioCase(6, block_id, 6, "MEDIUM", "OCCUPIED")
lockio7 = LockioCase(7, block_id, 7, "LARGE","DISABLED")
lockio8 = LockioCase(8, block_id, 8, "LARGE", "DISABLED")

@app.route('/api/rasp/1/lockios/<int:id>')
def get_Lockio(id):
    return jsonify(vars(LockioCase.getLockio(id)))


@app.route('/api/rasp/1/lockios/' , methods=['GET'])
def get_Lockios():
    lockios = LockioCase.getListeLockio()
    lockios_json = json.dumps([lockio.__dict__ for lockio in lockios])
    return lockios_json



@app.route('/api/rasp/1/lockios/<int:lockio_id>' , methods=['PATCH'] )
def patch_Lockio(lockio_id):
    lockio = LockioCase.getLockio(lockio_id)
    status = request.json['status']
    if lockio.status == 'AVAILABLE':
        lockio.status = status
    return jsonify(vars(lockio)),200



