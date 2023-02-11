from flask import Flask, render_template
from manage_leds import *
app = Flask(__name__, static_folder='static', static_url_path='/')


def run():
    app.run(debug=True, use_reloader=False, port=8000)


if __name__ == '__main__':
    run()


########
# ROUTES
########
@app.route('/')
def mainMenu():
    return app.send_static_file('index.html')


@app.route('/api/rasp/1/led/on')
def enableLeds():
    ledsOn()
    return "Leds on"


@app.route('/api/rasp/1/led/off')
def disableLeds():
    ledsOff()
    return "Leds off"
