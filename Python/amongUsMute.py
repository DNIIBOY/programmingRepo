import keyboard
from time import sleep

active = True
while active:
    sleep(1)
    keyboard.press_and_release("ctrl+F3")
