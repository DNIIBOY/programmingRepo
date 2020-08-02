#ORDHUSKER 3000
from tkinter import *

running = False

root = Tk()
root.minsize(height=40, width=70)
root.title("Kodehusker 3000")
root.resizable(0, 0)

def intro():
    global start
    global entry1
    start = Frame(root)
    start.pack(fill="x", expand=1)
    label1 = Label(start, text="Adgangskode: ", bg="white").grid(column=0)
    entry1 = Entry(start, bg="white", show="*")
    entry1.grid(row=0, column=1)
    b1 = Button(start, text="Next", command=check, width=7).grid(row=0, column=2)
    root.mainloop()


def write():
    try:
        koode = open("ikkeEnKode.txt", "r")
        if input("Hvad er koden?: ") == koode.read():
            koode.close()
            text = input("Hvad vil du gemme?: ")
            fil = open("john.txt", "w")
            fil.write(text)
            fil.close()
            print("Ord gemt")
    except:
        print("Der skete en fejl")

def read():
    try:
        koode = open("ikkeEnKode.txt", "r")
        if input("Hvad er koden?: ") == koode.read():
            koode.close()
            fil = open("john.txt", "r")
            print("Dit ord er: " + str(fil.read()))
    except:
        print("Der skete en fejl")

def koden():
    try:
        koode = open("ikkeEnKode.txt", "r")
        if input("Hvad er koden?: ") == koode.read():
            koode.close()
            koode = open("ikkeEnKode.txt", "w")
            nykode = input("Hvad skal den nye kode være?: ")
            koode.write(nykode)
        else:
            print("Forkert")
    except:
        print("Der skete en fejl")

def quit():
    run.destroy()
    global running
    running = False


def running():
    global run
    run = Frame(root)
    run.pack(fill="x", expand=1)

    bS = Button(run, text="Skriv").place(x=50, y=10)
    bL = Button(run, text="Læs ").place(x=90, y=10)
    bK = Button(run, text="Kode").place(x=130, y=10)
    bQ = Button(run, text="Quit", command = quit).place(x=175, y=10)

    root.mainloop()

def check():
    k = entry1.get()
    fil = open("ikkeEnKode.txt", "r")
    if k == fil.read():
        start.destroy()
        return running()
    fil.close()

intro()