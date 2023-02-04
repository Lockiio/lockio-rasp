import RPi.GPIO as GPIO
import time
from locker import Locker
from lockio import Lockio
GPIO.setmode(GPIO.BCM)

red = Locker("red",14,15)
brown = Locker("brown",18,23)
grey = Locker("grey",24,25)
orange = Locker("orange",12,16)
blue = Locker("blue",13,26)
green = Locker("green",4,17)
white = Locker("white",22,27)
purple = Locker("purple",5,6)

lockioProto = Lockio("proto")

lockioProto.addLockers([red,brown,grey,orange,blue,green,white,purple])

#NO NEEDED NORMALLY ==> understand why it turns orange when running script a 2nd time
lockioProto.switchOffRedAll()

lockioProto.switchOnGreenAll()
time.sleep(2)
lockioProto.switchOnRedAll()
time.sleep(2)
lockioProto.switchOffGreenAll()
time.sleep(2)
GPIO.cleanup()
