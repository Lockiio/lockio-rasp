from gpiozero import LED
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

# TODO FILE USED WHEN TESTING REMOTELY, NO USEFULL WHEN SERVER IS RUNNING ON RASPBERRY
raspberry = PiGPIOFactory(host='192.168.1.64')
red = LED(17, pin_factory=raspberry)


def testLeds():
    while True:
        red.on()
        sleep(1)
        red.off()
        sleep(1)
