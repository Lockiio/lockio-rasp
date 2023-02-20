import requests
import const.const as const
from flask import Flask, render_template
from manage_leds import *

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
