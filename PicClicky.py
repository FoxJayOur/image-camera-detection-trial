import pyautogui, sys
import keyboard
import time

while (True):
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.001
    pyautogui.moveTo(0,0)
    if (keyboard.is_pressed('p')):
        print("Stopped")
        exit(0)
    else:
        print("Not Clicking")