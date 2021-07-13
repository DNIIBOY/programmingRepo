import dearpygui.dearpygui as dpg
import os

dpg.setup_viewport()
dpg.set_viewport_title(title='Kodehusker v2.1')
dpg.set_viewport_width(275)
dpg.set_viewport_height(200)


def set_primary(window):
    dpg.set_primary_window(window, True)
    if window != mainwindow:
        dpg.set_primary_window(mainwindow, False)


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

        with dpg.window() as self.writeWindow:
            dpg.add_same_line(spacing=30)
            dpg.add_text("SKRIVVV")
            dpg.add_button(label='Skriv', height=30, width=60)
        dpg.hide_item(self.writeWindow)

        with dpg.window() as self.readWindow:
            dpg.add_same_line(spacing=30)
            dpg.add_text("LÆSS")
            dpg.add_button(label='Læs', height=30, width=60)
        dpg.hide_item(self.readWindow)

    def set_filename(self, filename: str):
        self.fileName = filename

    def toggle_write_window(self, mode: bool = True):
        if mode:
            dpg.show_item(self.writeWindow)
            dpg.hide_item(self.readWindow)
        else:
            dpg.hide_item(self.writeWindow)

    def toggle_read_window(self, mode: bool = True):
        if mode:
            dpg.show_item(self.readWindow)
            dpg.hide_item(self.writeWindow)
        else:
            dpg.hide_item(self.readWindow)

if __name__ == '__main__':
    w = WordSaver()

    with dpg.window() as mainwindow:
        dpg.add_same_line(spacing=45)
        dpg.add_text("Filnavn:")
        dpg.add_same_line(spacing=5)
        dpg.add_input_text(label='.txt', hint="Filename", width=65,
                           callback=lambda sender: w.set_filename(dpg.get_value(sender)),
                           no_spaces=True, default_value=w.fileName)
        dpg.add_spacing(count=5)
        dpg.add_same_line(spacing=75)
        dpg.add_button(label="Skriv", callback=w.toggle_write_window)
        dpg.add_same_line(spacing=10)
        dpg.add_button(label="Læs", callback=w.toggle_read_window)

    set_primary(mainwindow)
    dpg.start_dearpygui()
