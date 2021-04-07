import keyboard
from PIL import ImageGrab as imggrab
from time import sleep

# Task Indicator
# imggrab.grab(bbox=(561, 230, 562, 231)).getpixel((0, 0)) == (255, 255, 255)
# imggrab.grab(bbox=(19, 235, 20, 236)).getpixel((0, 0)) == (255, 255, 255)

# Meeting Screen:
# imggrab.grab(bbox=(1219, 609, 1220, 610)).getpixel((0, 0)) == (170, 200, 229)

# Meeting Dead:
# imggrab.grab(bbox=(1219, 609, 1220, 610)).getpixel((0, 0)) == (36, 43, 46)

#Task Bar:
# imggrab.grab(bbox=(300, 25, 301, 26)).getpixel((0, 0)) == (170, 187, 187)

def shouldBeMuted():
    if imggrab.grab(bbox=(300, 25, 301, 26)).getpixel((0, 0)) == (170, 187, 187):
        screenImgClr = imggrab.grab(bbox=(1219, 609, 1220, 610)).getpixel((0, 0))
        return not (screenImgClr == (170, 200, 229) or screenImgClr == (24, 121, 2) or screenImgClr == (255, 0, 0))
    else:
        return False


print("Among Us automuter\nby: Daniel Nettelfield")

muted = shouldBeMuted()
if muted:
    keyboard.press_and_release("ctrl+F3")
print("Mic Off" if muted else "Mic On")
sleep(2)


while True:
    gameStatus = shouldBeMuted()
    if muted != gameStatus:
        keyboard.press_and_release("ctrl+F3")
        muted = gameStatus
        print("Mic Off" if gameStatus else "Mic On")
    sleep(.5)
