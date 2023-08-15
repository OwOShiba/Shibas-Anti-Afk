import win32gui
import time

the_window_hwnd = win32gui.GetForegroundWindow()  # hwnd of the specific window, it could be whatever you what
left_top_x, left_top_y, *useless_position = win32gui.GetWindowRect(the_window_hwnd) # get the position of window you gave.

mouse_pos_x, mouse_pos_y = win32gui.GetCursorPos()
pos_in_window_x, pos_in_window_y = (mouse_pos_x - left_top_x), (mouse_pos_y - left_top_y)

def getWindowSize(window):
    rect = win32gui.GetWindowRect(window)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return w, h
