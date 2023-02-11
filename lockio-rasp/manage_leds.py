from lockio import Lockio
from block import Block

red = Lockio("red", 14, 15)
brown = Lockio("brown", 18, 23)
grey = Lockio("grey", 24, 25)
orange = Lockio("orange", 12, 16)
blue = Lockio("blue", 13, 26)
green = Lockio("green", 4, 17)
white = Lockio("white", 22, 27)
purple = Lockio("purple", 5, 6)

block = Block("proto")
block.addLockios([red, brown, grey, orange, blue, green, white, purple])


def ledsOn():
    block.switchOnAll("green")


def ledsOff():
    block.switchOffAll("green")
