import dearpygui.dearpygui as dpg
import os

dpg.setup_viewport()
dpg.set_viewport_title(title='Kodehusker v2.1')
dpg.set_viewport_width(275)
dpg.set_viewport_height(200)


def set_primary(window):
    dpg.set_primary_window(window, True)


def find_aes_file() -> str:
    files = os.listdir(os.getcwd())
    for file in files:
        if file[-8:] == ".txt.aes":
            return file[:-8]
    return ""

def printFN():
    print(w.fileName)

class WordSaver:
    def __init__(self):
        self.fileName = find_aes_file()

    def setfilename(self, filename):
        self.fileName = filename


if __name__ == '__main__':
    w = WordSaver()

    with dpg.window() as mainwindow:
        dpg.add_same_line(spacing=45)
        dpg.add_text("Filnavn:")
        dpg.add_same_line(spacing=5)
        dpg.add_input_text(label='.txt', hint="Filename", width=65,
                           callback=lambda sender: w.setfilename(dpg.get_value(sender)),
                           no_spaces=True, default_value=w.fileName)
        dpg.add_spacing(count=5)
        dpg.add_same_line(spacing=75)
        dpg.add_button(label="Skriv", callback=printFN)
        dpg.add_same_line(spacing=10)
        dpg.add_button(label="Læs")

    set_primary(mainwindow)
    dpg.start_dearpygui()
