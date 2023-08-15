from shiba.SolveAntiAfk import *
from shiba.Movements import *
from shiba.Utils import *
import time
import win32gui
import pywinauto 

def getSizeDiff(window):
    origX = 1920
    origY = 1080
    newX, newY = getWindowSize(window)
    Xdiff = int(math.floor(newX/origX))
    Ydiff = int(math.floor(newY/origY))
    return Xdiff, Ydiff

def wait(n):
    time.sleep(n)

def pressAntiAFK(diff1, diff2, x1, y1):
    MoveMouse(520 * diff1, 775 * diff2)
    wait(.1)
    MouseClick('left')
    wait(.01)
    pydirectinput.leftClick((521-x1) * diff1, (776-y1) * diff2, .1, .1)
    wait(.01)
    MouseClick('left')
    wait(.1)
    MoveMouse(900, 500)

def movearound(x1, y1):
    KeyDown('w')
    wait(.3)
    KeyUp('w')
    MouseClick('left')
    KeyDown('a')
    wait(.3)
    KeyUp('a')
    RandomDrag(x1, y1)
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
    RandomDrag(x1, y1)
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
    RandomDrag(x1, y1)
    wait(.3)

def Start(ae):
    print("started")

pydirectinput.FAILSAFE = False
def Start():
    while True:
        windows = pywinauto.Desktop(backend="uia").windows()
        for w in windows:
            if w.window_text() == "Roblox":
                w.set_focus()
                handle = w.handle
                sizeDiffX, sizeDiffY = getSizeDiff(handle)
                x, y, x1, y1 = win32gui.GetClientRect(handle)
                wait(3)
                movearound(x, y)
                wait(.1)
                pressAntiAFK(sizeDiffX, sizeDiffY, x, y)
                wait(.5)
                text = GIVEMEIT(handle, x, y)
                if text != "False":
                    pydirectinput.moveTo((1714-x) * sizeDiffX, (1025-y) * sizeDiffY)
                    wait(.1)
                    MouseClick('left')
                    wait(.01)
                    pydirectinput.leftClick((1715-x) * sizeDiffX, (1026-y) * sizeDiffY)
                    wait(.01)
                    MouseClick('left')
                    wait(.1)
                    pydirectinput.write(text, .15)
                    PressKey('enter')
                wait(5) # I LVOE STAYLOR SWIFT


