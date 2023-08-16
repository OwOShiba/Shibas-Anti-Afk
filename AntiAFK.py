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

def pressAntiAFK(diff1, diff2, x1, y1, x, y):
    MoveMouse((520 * diff1) + x, (775 * diff2) + y)
    wait(.1)
    MouseClick('left')
    wait(.01)
    pydirectinput.leftClick((521* diff1) + x, (776* diff2)+y, .1, .1)
    wait(.01)
    MouseClick('left')
    wait(.1)
    MoveMouse(900, 500)

def movearound(x, y, x1, y1):
    KeyDown('w')
    wait(.3)
    KeyUp('w')
    MouseClick('left')
    KeyDown('a')
    wait(.3)
    KeyUp('a')
    RandomDrag(x, y, x1, y1)
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
    RandomDrag(x, y, x1, y1)
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
    RandomDrag(x, y, x1, y1)
    wait(.3)
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
                print(win32gui.GetClientRect(handle))
                wait(3)
                movearound(x, y, x1, y1)
                wait(.1)
                pressAntiAFK(sizeDiffX, sizeDiffY, x1, y1, x, y)
                wait(.5)
                text = GIVEMEIT(handle, x, y)
                if text != "False":
                    pydirectinput.moveTo(((1714)-(1714-x1)) * sizeDiffX, ((1025)-(1025-y1)) * sizeDiffY)
                    wait(.1)
                    MouseClick('left')
                    wait(.01)
                    pydirectinput.leftClick(((1714)-(1714-x1)) * sizeDiffX, ((1025)-(1025-y1)) * sizeDiffY)
                    wait(.01)
                    MouseClick('left')
                    wait(.1)
                    pydirectinput.write(text, .15)
                    PressKey('enter')
                wait(5) # I LVOE STAYLOR SWIFT