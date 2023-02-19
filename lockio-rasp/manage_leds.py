from lockio import Lockio
from block import Block

red = Lockio("red")
brown = Lockio("brown")
grey = Lockio("grey")
orange = Lockio("orange")
blue = Lockio("blue")
green = Lockio("green")
white = Lockio("white")
purple = Lockio("purple")

block = Block("proto")
block.addLockios([red, brown, grey, orange, blue, green, white, purple])


def ledsOn():
    block.switchOnAll("green")


def ledsOff():
    block.switchOffAll("green")
