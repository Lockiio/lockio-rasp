import requests
import const.const as const
from flask import Flask, render_template
from manage_leds import *
app = Flask(__name__)


def run():
    app.run(debug=True, use_reloader=False, port=8000)

# Use to run function at start of flask server
with app.app_context():
    def getLockiosStatus():
        response = requests.get(const.BACK_URL)
        return response.json()
        # TODO GET INFO FOR EACH LOCKIOS AND LIGHT THE LEDS WITH THEIR CORRECT STATUS
    getLockiosStatus()
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
