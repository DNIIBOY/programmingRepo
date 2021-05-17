from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

sleep(3)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:

    sleep(0.003)

    if pyautogui.pixel(820, 570)[0] == 17:
        click(800, 570)
    if pyautogui.pixel(920, 570)[0] == 17:
        click(900, 570)
    if pyautogui.pixel(1020, 570)[0] == 17:
        click(1000, 570)
    if pyautogui.pixel(1120, 570)[0] == 17:
        click(1100, 570)