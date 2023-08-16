import sys
import pytesseract
import pydirectinput
from PIL import Image
import re
import math
from Utils import *

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

try:
    from PIL import ImageGrab
    use_grab = True
except Exception as ex:
    raise ex

def getSizeDiff(window):
    origX = 1920
    origY = 1080
    newX, newY = getWindowSize(window)
    Xdiff = (newX/origX)
    Ydiff = (newY/origY)
    return Xdiff, Ydiff

def screenGrab( rect ):
    global use_grab
    x, y, width, height = rect

    if ( use_grab ):
        image = ImageGrab.grab( bbox=[ x, y, x+width, y+height ] )
    else:
        return
    return image

def GIVEMEIT(window, x1, y1):
    print("giving")
    # print(x1, y1)
    diff1, diff2 = getSizeDiff(window)
    x = (1652* diff1) + x1
    y = (965* diff2) + y1
    width  = 160 * diff1
    height = 32 * diff2
    # print(x, y, width, height)

    # Area of screen to monitor
    screen_rect = [ x, y, width, height ]  
    image = screenGrab( screen_rect )              # Grab the area of the screen
    text  = pytesseract.image_to_string( image )   # OCR the image

    # IF the OCR found anything, write it to stdout.
    text = text.strip()
    print(text)
    if ( len( text ) > 0 ):
        if text.find("+") != -1:
            test = text.split("+")
            print(test)
            t1 = re.sub('[^0-9]','', test[0])
            t2 = re.sub('[^0-9]','', test[1])
            add = int(t1) + int(t2)
            print(add)
            return str(add)
        if text.find("-") != -1:
            test = text.split("-")
            t1 = re.sub('[^0-9]','', test[0])
            t2 = re.sub('[^0-9]','', test[1])
            sub = int(t1) - int(t2)
            print(sub)
            return str(sub)
        else:
            return "a"
    else:
        return "a"