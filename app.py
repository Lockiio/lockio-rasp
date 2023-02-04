from flask import Flask, render_template
from static.remote_connexion import testLeds, ledsOn, ledsOff
app = Flask(__name__)
import routes.lockio_routes




@app.route('/')
def hello_world():
    return render_template("index.html")


with app.app_context():
    testLeds()


def run():
    app.run(debug=True, use_reloader=False)


if __name__ == '__main__':
    run()
    # TODO AT START OF SERVER, GET THE STATUS OF ALL THE LOCKIOS IN THE MYSQL DATABASE (ON SPRING)
