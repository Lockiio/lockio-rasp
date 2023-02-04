from flask import Flask, render_template
from remote_connexion import testLeds

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/led')
def enableLeds():
    testLeds()

with app.app_context():
    testLeds()

def run():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    run()
    # TODO AT START OF SERVER, GET THE STATUS OF ALL THE LOCKIOS IN THE MYSQL DATABASE (ON SPRING)
