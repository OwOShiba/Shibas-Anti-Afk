import time
import random
import pydirectinput

def PressKey(key):
    pydirectinput.press(key)

def KeyDown(key):
    pydirectinput.keyDown(key)

def KeyUp(key):
    pydirectinput.keyUp(key)

def MoveMouse(x,y):
    pydirectinput.moveTo(x, y, .3)

def MouseClick(butt):
    pydirectinput.click(button=butt, clicks=2, interval=.1)

def MouseHold(butt, dur):
    pydirectinput.mouseDown(button=butt)
    time.sleep(dur)
    pydirectinput.mouseUp(button=butt)

def RandomDrag():
    pydirectinput.mouseDown(button='right')
    pydirectinput.moveTo(random.randint(500, 1400), random.randint(200, 800), .3)
    pydirectinput.mouseUp(button='right')