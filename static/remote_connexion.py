from time import sleep

from static.locker import Locker
from static.lockio import Lockio

red = Locker("red", 14, 15)
brown = Locker("brown", 18, 23)
grey = Locker("grey", 24, 25)
orange = Locker("orange", 12, 16)
blue = Locker("blue", 13, 26)
green = Locker("green", 4, 17)
white = Locker("white", 22, 27)
purple = Locker("purple", 5, 6)

lockioProto = Lockio("proto")
lockioProto.addLockers([red, brown, grey, orange, blue, green, white, purple])
def testLeds():
    lockioProto.switchOnGreenAll()

def ledsOn():
    lockioProto.switchOnGreenAll()

def ledsOff():
    lockioProto.switchOffGreenAll()

testLeds()
