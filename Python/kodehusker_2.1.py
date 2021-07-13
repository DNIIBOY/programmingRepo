import dearpygui.dearpygui as dpg
import os

wide, high = (275, 250)

dpg.setup_viewport()
dpg.set_viewport_title(title='Kodehusker v2.1')
dpg.set_viewport_width(wide)
dpg.set_viewport_height(high)

dpg.set_viewport_max_width(wide)
dpg.set_viewport_min_width(wide)
dpg.set_viewport_max_height(high)
dpg.set_viewport_min_height(high)


def find_aes_file() -> str:
    # Finder første fil med rigtige krypteringstype
    files = os.listdir(os.getcwd())
    for file in files:
        if file[-8:] == ".txt.aes":  # Bruger filnavnet til at vurdere krypteringstype
            return file[:-8]
    return ""


class WordSaver:
    def __init__(self):

        self.fileName = find_aes_file()  # Set filnavnet af objektet til senere brug
        self.encryptetFileName = self.fileName + ".aes"


        with dpg.window(no_resize=True) as self.mainWindow:
            # Laver hovedvindet med alle items
            dpg.add_same_line(spacing=45)
            dpg.add_text("Filnavn:")
            dpg.add_same_line(spacing=5)
            # Laver input textfelt, som selv ændrer WordSaver.filename
            dpg.add_input_text(label='.txt', hint="Filename", width=65,
                               callback=lambda sender: self.set_filename(dpg.get_value(sender)),
                               no_spaces=True, default_value=self.fileName)
            dpg.add_spacing(count=5)
            dpg.add_same_line(spacing=75)
            dpg.add_button(label="Skriv", callback=self.toggle_write_window)
            dpg.add_same_line(spacing=10)
            dpg.add_button(label="Læs", callback=self.toggle_read_window)
            # Dette textfelt bruges til Input og Output til filen
            dpg.add_input_text(multiline=True, width=wide-50, height=100, pos=[15, 90], label='')


        with dpg.window(label="Skriv", no_collapse=True, show=False, pos=[80, 80]) as self.writeWindow:
            # Skaber vinduet til at skrive til krypteringsfilen. Skjult som default.
            dpg.add_same_line(spacing=30)
            dpg.add_text("SKRIVVV", )
            dpg.add_button(label='Skriv', height=30, width=60)


        with dpg.window(label="Læs", no_collapse=True, show=False, width=200, height=100,
                        pos=[30, 80], no_resize=True, no_move=True) as self.readWindow:
            # Laver vinduet til at læse fra krypteringsfilen. Skjult som default
            dpg.add_same_line(spacing=5)
            dpg.add_text(f"Kode:")
            dpg.add_same_line(spacing=10)
            # Adgangskodefelt. Kalder samme funktion som "Læs" knappen (show_read_text)
            dpg.add_input_text(password=True, hint="password", label="", on_enter=True, callback=None)
            dpg.add_spacing(count=3)
            dpg.add_same_line(spacing=70)
            dpg.add_button(label='Læs', height=30, width=60)


    def set_filename(self, filename: str):
        # Funktion tillader filnavnskift
        self.fileName = filename


    def toggle_write_window(self, mode: bool = True):
        # Denne funktion skjuler / viser vinduet til at skrive til filen
        if mode:
            dpg.show_item(self.writeWindow)
            dpg.hide_item(self.readWindow)
        else:
            dpg.hide_item(self.writeWindow)  # Skjuler modsatte vindue hvis åbnet


    def toggle_read_window(self, mode: bool = True):
        # Skjuler / viser vindet til at læse fra filen
        if mode:
            dpg.show_item(self.readWindow)
            dpg.hide_item(self.writeWindow)
        else:
            dpg.hide_item(self.readWindow)  # Skjuler modsatte vindue

    def show_read_text(self):
        # Denne funktion tager teksten fra krypteret fil og indsætter i mainWindow tekstfelt
        pass


if __name__ == '__main__':
    w = WordSaver()

    dpg.set_primary_window(w.mainWindow, True)
    dpg.start_dearpygui()
