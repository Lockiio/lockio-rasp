import requests
from flask import Flask, render_template
from manage_leds import ledsOn, ledsOff

app = Flask(__name__, static_folder='static', static_url_path='/')
import routes.lockio_routes


@app.route('/')
def mainMenu():
    return app.send_static_file('index.html')


with app.app_context():
    #TODO MOVE THIS TO ROUTE FILE SPECIALY FOR BACKEND
    def getLockiosStatus():
        import const.const as const
        response = requests.get(const.BACK_URL)
        return response.json()
        # TODO GET INFO FOR EACH LOCKIOS AND SHOW LIGHT THE LEDS WITH THEIR CORRECT STATUS
    getLockiosStatus()
    ledsOn()


def run():
    app.run(debug=True, use_reloader=False)


if __name__ == '__main__':
    run()
