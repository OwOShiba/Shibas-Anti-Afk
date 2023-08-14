import sys
import pytesseract
import pydirectinput
from PIL import Image
import re
import math

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

try:
    from PIL import ImageGrab
    use_grab = True
except Exception as ex:
    if ( sys.platform == 'linux' ):
        from Xlib import display, X   
        use_grab = False
    else:
        raise ex

def getSizeDiff():
    origX = 1920
    origY = 1080
    newX, newY = pydirectinput.size()
    Xdiff = int(math.floor(newX/origX))
    Ydiff = int(math.floor(newY/origY))
    return Xdiff, Ydiff

def screenGrab( rect ):
    """ Given a rectangle, return a PIL Image of that part of the screen.
        Handles a Linux installation with and older Pillow by falling-back
        to using XLib """
    global use_grab
    x, y, width, height = rect

    if ( use_grab ):
        image = ImageGrab.grab( bbox=[ x, y, x+width, y+height ] )
    else:
        # ImageGrab can be missing under Linux
        dsp  = display.Display()
        root = dsp.screen().root
        raw_image = root.get_image( x, y, width, height, X.ZPixmap, 0xffffffff )
        image = Image.frombuffer( "RGB", ( width, height ), raw_image.data, "raw", "BGRX", 0, 1 )
        # DEBUG image.save( '/tmp/screen_grab.png', 'PNG' )
    return image

def GIVEMEIT():
    print("giving")
    diff1, diff2 = getSizeDiff()
    x = 1652 * diff1
    y = 965 * diff2
    width  = 160 * diff1
    height = 32 * diff2

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
            return "I'm bad at math.."
    else:
        return "No Anti-Afk yet!"