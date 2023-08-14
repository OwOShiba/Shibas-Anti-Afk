from shiba.SolveAntiAfk import *
from shiba.Movements import *
import time

diff1, diff2 = getSizeDiff()

def wait(n):
    time.sleep(n)

def pressAntiAFK():
    MoveMouse(520 * diff1, 775 * diff2)
    wait(.1)
    MouseClick('left')
    wait(.01)
    pydirectinput.leftClick(521 * diff1, 776 * diff2, .1, .1)
    wait(.01)
    MouseClick('left')
    wait(.1)
    MoveMouse(900, 500)

def movearound():
    KeyDown('w')
    wait(.3)
    KeyUp('w')
    MouseClick('left')
    KeyDown('a')
    wait(.3)
    KeyUp('a')
    RandomDrag()
    KeyDown('s')
    wait(.3)
    KeyUp('s')
    MouseClick('left')
    KeyDown('d')
    wait(.3)
    KeyUp('d')
    KeyDown('w')
    wait(.3)
    KeyUp('w')
    RandomDrag()
    KeyDown('a')
    wait(.3)
    KeyUp('a')
    MouseClick('left')
    KeyDown('s')
    wait(.3)
    KeyUp('s')
    MouseClick('left')
    KeyDown('d')
    wait(.3)
    KeyUp('d')
    RandomDrag()
    wait(.3)

pydirectinput.FAILSAFE = False
while True:
    wait(3)
    movearound()
    wait(.1)
    pressAntiAFK()
    wait(.5)
    text = GIVEMEIT()
    if text != "False":
        pydirectinput.moveTo(1714 * diff1, 1025 * diff2)
        wait(.1)
        MouseClick('left')
        wait(.01)
        pydirectinput.leftClick(1715 * diff1, 1026 * diff2)
        wait(.01)
        MouseClick('left')
        wait(.1)
        pydirectinput.write(text, .15)
        PressKey('enter')
    wait(22) # I LVOE STAYLOR SWIFT


