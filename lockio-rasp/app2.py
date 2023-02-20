from flask import Flask, render_template, jsonify
from stubLockio import stubLockio
app = Flask(__name__)

lockio1 = stubLockio(1, "OCCUPIED")
lockio2 = stubLockio(2, "AVAILABLE")



@app.route('/api/rasp/v1/lockio/<int:id>/test')
def get_Lockio(id):
    return jsonify(vars(stubLockio.getLockio(id)))


@app.route('/api/rasp/v1/lockios')
def get_Lockios():
    return jsonify(vars(stubLockio.getListeLockio()));

@app.route('/api/rasp/v1/lockio/<int:lockio_id>' , methods=['PATCH'])
def patch_Lockio(lockio_id):
    lockio = stubLockio.getLockio(lockio_id)
    status = request.json['status']
    if lockio.status == 'AVAILABLE':
        lockio.status = status
        return jsonify(lockio.serialize()), 200
    else:
        return '', 204


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)




