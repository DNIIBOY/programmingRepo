import keyboard
from PIL import ImageGrab as imggrab
from time import sleep

def getInGameStatus():
    img = imggrab.grab(bbox=(1850, 178, 1851, 179))
    rgb_pixel_value = img.getpixel((0, 0))

    if rgb_pixel_value == (238, 238, 238):
        return True
    else:
        return False

print("Among Us automuter\nby: Daniel Nettelfield")

muted = getInGameStatus()
if muted:
    keyboard.press_and_release("ctrl+F3")
sleep(2)

while True:
    gameStatus = getInGameStatus()
    if muted != gameStatus:
        keyboard.press_and_release("ctrl+F3")
        muted = gameStatus
        print(gameStatus)
    sleep(2)
