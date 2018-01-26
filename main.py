import pyautogui, time, threading, psutil, sys
from win32 import win32gui, win32process
from tkinter import *

def active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        pass

def print_no_newline(string):
    sys.stdout.write("\r")
    sys.stdout.write(string)
    sys.stdout.flush()

print('Ctrl + C to abort.')
try:
    while True:
        x, y = pyautogui.position()
        pixelColor = pyautogui.pixel(x, y)
        activeWindow = ' Active Window:' + str(active_window_process_name() if active_window_process_name() else '').rjust(15)
        ss = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        ss += ' RGB: (' + str(pixelColor[0]).rjust(3)
        ss += ', ' + str(pixelColor[1]).rjust(3)
        ss += ', ' + str(pixelColor[2]).rjust(3) + ')'
        # if pyautogui.pixelMatchesColor(1140, 400, (255, 0, 0)):
        #     ss += ' Red'
        ss += activeWindow
        print_no_newline(ss)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nDone...")

#width, height = pyautogui.size()

#for i in range(3):
  #  pyautogui.moveTo(100, 100, duration=0.25)
  #  pyautogui.moveTo(200, 100, duration=0.25)
  #  pyautogui.moveTo(200, 200, duration=0.25)
  #  pyautogui.moveTo(100, 200, duration=0.25)

#for i in range(3):
  #  pyautogui.moveRel(100, 0, duration=0.25)
  # pyautogui.moveRel(0, 100, duration=0.25)
  #  pyautogui.moveRel(-100, 0, duration=0.25)
  #  pyautogui.moveRel(0, -100, duration=0.25)
