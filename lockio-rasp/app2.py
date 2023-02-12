from flask import Flask, render_template, jsonify
from stubLockio import stubLockio
app = Flask(__name__)

lockio1 = stubLockio(1, "OCCUPIED")
lockio2 = stubLockio(2, "OCCUPIED")


@app.route('/<int:id>/status')
def get_Lockio(id):
    return jsonify(vars(stubLockio.getLockio(id)))


if __name__ == "__main__":
    app.run(debug=True)

