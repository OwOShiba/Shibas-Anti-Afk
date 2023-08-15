import time
import random
import pydirectinput
def coords(x, y):
    origX = 1920
    origY = 1080
    newX, newY = pydirectinput.size()
    Xdiff = newX/origX
    Ydiff = newY/origY
    xx = x * Xdiff
    yy = y * Ydiff
    return xx, yy

def getSizeDiff():
    origX = 1920
    origY = 1080
    newX, newY = pydirectinput.size()
    Xdiff = int(newX/origX)
    Ydiff = int(newY/origY)
    return Xdiff, Ydiff

def PressKey(key):
    pydirectinput.press(key)

def KeyDown(key):
    pydirectinput.keyDown(key)

def KeyUp(key):
    pydirectinput.keyUp(key)

def MoveMouse(x,y):
    pydirectinput.moveTo(x, y, duration=.3)

def MouseClick(butt):
    pydirectinput.click(button=butt, clicks=2, interval=.1)

def MouseHold(butt, dur):
    pydirectinput.mouseDown(button=butt)
    time.sleep(dur)
    pydirectinput.mouseUp(button=butt)

def RandomDrag(x1, y1):
    diff1, diff2 = getSizeDiff()
    pydirectinput.mouseDown(button='right')
    pydirectinput.moveTo(random.randint((500-x1) * diff1, (1400-y1) * diff2), random.randint((200-x1) * diff1, (800-y1) * diff2), .3)
    pydirectinput.mouseUp(button='right')