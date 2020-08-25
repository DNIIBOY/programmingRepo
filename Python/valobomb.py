from tkinter import *
import pyscreenshot as imggrab
from time import sleep

global bombstatus
global counting
global bombtime
bombstatus = False
counting = False
bombtime = 45

def setup():
    global root
    global t
    root = Tk()
    root.title("Valorant Bomb Timer")
    root.geometry("300x200")
    root.resizable(False, False)
    t = StringVar()
    t.set("45")
    lb = Label(root, textvariable=t)
    lb.config(font=("Courier 40 bold"))
    bt1 = Button(root, text="Start", command=main, font=("Courier 12 bold"))
    bt2 = Button(root, text="Start Timer", command=start_timer, font=("Courier 12 bold"))
    lb.place(x=120, y=10)
    bt1.place(x=120, y=100)
    bt2.place(x=120, y=150)

def get_bomb_status():
    img = imggrab.grab(bbox=(945, 27, 946, 28))
    rgb_pixel_value = img.getpixel((0, 0))

    if rgb_pixel_value == (230, 0, 0) or rgb_pixel_value == (170, 0, 0):
        return True
    else:
        return False


def main():
    global bombtime
    global counting
    status = get_bomb_status()
    if status == True and bombtime >=0 and counting == False:
        counting = True
        start_timer()
    elif status == False and counting == True:
        counting = False
        sleep(2)
        reset()
    print(status)
    root.after(930, main())

def start_timer():
    global counting
    counting = True
    timer()

def reset():
    global t
    t.set("45")

def timer():
    global counting
    global bombtime
    global t
    if (counting == True):
        d = str(t.get())
        bombtime = int(d)
        if (bombtime > 0):
            bombtime -= 1
        d = bombtime
        t.set(d)


setup()

root.mainloop()