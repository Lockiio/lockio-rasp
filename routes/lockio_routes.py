from app import app
from manage_leds import ledsOn, ledsOff

# TODO CHANGE ROUTES ENDPOINTS

@app.route('/api/rasp/1/led/on')
def enableLeds():
    ledsOn()
    return "Leds on"

@app.route('/api/rasp/1/led/off')
def disableLeds():
    ledsOff()
    return "Leds off"