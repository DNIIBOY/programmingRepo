import pyperclip
import keyboard
from time import sleep

while True:
    if keyboard.is_pressed("Ctrl+Shift+V"):
        x = pyperclip.paste()
        print("Before: ", x)
        for i in range(len(x)):
            if not x[0].isalnum():
                x = x[1:]
            else:
                break
        pyperclip.copy(x)
        print("After: ", x)
        sleep(0.5)
