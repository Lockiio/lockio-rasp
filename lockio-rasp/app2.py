from flask import Flask, render_template, jsonify, request
from LockioCase import LockioCase

app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)




