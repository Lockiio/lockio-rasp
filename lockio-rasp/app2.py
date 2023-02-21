from flask import Flask, render_template, jsonify, request
from Lockio import Lockio

app = Flask(__name__)

block_id= 1;
lockio1 = Lockio(1, block_id, 1, "SMALL","OCCUPIED")
lockio2 = Lockio(2, block_id, 2,"SMALL", "AVAILABLE")
lockio3 = Lockio(3, block_id, 3, "MEDIUM", "AVAILABLE")
lockio4 = Lockio(4, block_id, 4, "MEDIUM", "AVAILABLE")
lockio5 = Lockio(5, block_id, 5, "MEDIUM", "OCCUPIED")
lockio6 = Lockio(6, block_id, 6, "MEDIUM", "OCCUPIED")
lockio7 = Lockio(7, block_id, 7, "LARGE","DISABLED")
lockio8 = Lockio(8, block_id, 8, "LARGE", "DISABLED")

@app.route('/api/rasp/1/lockios/<int:id>')
def get_Lockio(id):
    return jsonify(vars(Lockio.getLockio(id)))


@app.route('/api/rasp/1/lockios/' , methods=['GET'])
def get_Lockios():
    lockios = Lockio.getListeLockio()
    lockios_json = json.dumps([lockio.__dict__ for lockio in lockios])
    return lockios_json



@app.route('/api/rasp/1/lockios/<int:lockio_id>' , methods=['PATCH'] )
def patch_Lockio(lockio_id):
    lockio = Lockio.getLockio(lockio_id)
    status = request.json['status']
    if lockio.status == 'AVAILABLE':
        lockio.status = status
    return jsonify(vars(lockio)),200



if __name__ == '__main__':
    app.run(debug=True)




