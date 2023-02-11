from app import app
from static.remote_connexion import ledsOn, ledsOff

# TODO CHANGE ROUTES ENDPOINTS
@app.route('/led/on')
def enableLeds():
    ledsOn()

@app.route('/led/off')
def disableLeds():
    ledsOff()