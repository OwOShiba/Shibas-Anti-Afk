import PySimpleGUI as sg
import sys
sys.path.append("../Shibas-Anti-Afk")
from AntiAFK import *

layout = [[sg.Text("All hail shiba")],
          [sg.Button('Start')]]

# Create the window
window = sg.Window('Shibas AntiAFK', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Start":
        wait(.5)
        Start()
        

window.close()