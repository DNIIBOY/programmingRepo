from tkinter import *

root = Tk()
root.minsize(height = 40, width=70)
root.title("Kodehusker 3000")
root.geometry("261x50")
root.resizable(0, 0)

run = Frame(root)
run.pack(fill = "x", expand =1)

bS = Button(text="Skriv").place(x=50, y=10)
bL = Button(text="Læs ").place(x=90, y=10)
bK = Button(text="Kode").place(x=130, y=10)
bQ = Button(text="Quit", command = quit).place(x=175, y=10)

root.mainloop()