from pyautogui import *
from time import sleep
from keyboard import press_and_release, is_pressed
import sys

try:
    speed = float(input("Hvor lang tid mellem hvert ord? (sek): "))
except ValueError:
    print("Ikke et tal din botnak")

def setcolor():
    click(435, 120)
    sleep(0.4)
    click(435, 140)

def run(delay):
    setcolor()
    press_and_release("right")
    while not is_pressed('q'):
        click(425, 120)
        sleep(delay)
        press_and_release("control + right")
        press_and_release("right")

    press_and_release("control + a")
    click(425, 120)
    press_and_release("right")
    press_and_release("backspace")
    sleep(0.2)
    press_and_release("space")
    sleep(0.1)
    press_and_release("backspace")

while True:
    if is_pressed("s"):
        press_and_release("backspace")
        run(speed)
    elif is_pressed("q"):
        sys.exit()
