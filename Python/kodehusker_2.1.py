import dearpygui.dearpygui as dpg
import os
import pyAesCrypt

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

        self.bufferSize = 64 * 1024

        self.fileName = find_aes_file()  # Set filnavnet af objektet til senere brug

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
            self.statusGood = dpg.add_text("", color=[0, 255, 0], show=False, pos=[10, 70])
            self.statusBad = dpg.add_text("", color=[255, 0, 0], show=False, pos=[10, 70])
            dpg.add_text("Text der skal krypteres:", pos=[40, 85])
            # Dette textfelt bruges til Input og Output til filen
            self.rwfield = dpg.add_input_text(multiline=True, width=wide - 50, height=90, pos=[15, 110], label='')

        with dpg.window(label="Skriv", no_collapse=True, show=False, width=200, height=20,
                        pos=[30, 10], no_resize=True, no_move=True) as self.writeWindow:
            # Skaber vinduet til at skrive til krypteringsfilen. Skjult som default.
            dpg.add_same_line(spacing=5)
            dpg.add_text("Kode:")
            dpg.add_same_line(spacing=10)
            # Adgangskodefelt. Kalder samme funktion som "Læs" knappen (show_read_text)
            self.writePW = dpg.add_input_text(password=True, hint="password", label="",
                                              on_enter=True, callback=self.write_text)
            dpg.add_spacing(count=3)
            dpg.add_same_line(spacing=70)
            dpg.add_button(label='Skriv', height=30, width=60, callback=self.write_text)

        with dpg.window(label="Læs", no_collapse=True, show=False, width=200, height=20,
                        pos=[30, 10], no_resize=True, no_move=True) as self.readWindow:
            # Laver vinduet til at læse fra krypteringsfilen. Skjult som default
            dpg.add_same_line(spacing=5)
            dpg.add_text(f"Kode:")
            dpg.add_same_line(spacing=10)
            # Adgangskodefelt. Kalder samme funktion som "Læs" knappen (show_read_text)
            self.readPW = dpg.add_input_text(password=True, hint="password", label="",
                                             on_enter=True, callback=self.read_text)
            dpg.add_spacing(count=3)
            dpg.add_same_line(spacing=70)
            dpg.add_button(label='Læs', height=30, width=60, callback=self.read_text)

        self.fileName = self.fileName + ".txt"  # Sætter rigtige filnavne med typer
        self.encryptetFileName = self.fileName + ".aes"  # .aes er krypteringstypen

    def show_error(self, error):
        dpg.add_spacing(count=35, parent=self.mainWindow)
        dpg.add_text(error, color=[255, 0, 0], parent=self.mainWindow)

    def show_status(self, status: str, good: bool):
        if good:
            dpg.show_item(self.statusGood)
            dpg.hide_item(self.statusBad)
            dpg.set_value(self.statusGood, status)
        elif not good:
            dpg.show_item(self.statusBad)
            dpg.hide_item(self.statusGood)
            dpg.set_value(self.statusBad, status)

    def set_filename(self, filename: str):
        # Funktion tillader filnavnskift
        self.fileName = filename + ".txt"
        self.encryptetFileName = self.fileName + ".aes"

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

    def delete_txt(self):
        # Denne funktion sletter .txt filen, som ikke er krypteret
        os.remove(self.fileName)

    def encrypt(self, key: str) -> bool:
        try:
            pyAesCrypt.encryptFile(self.fileName, self.encryptetFileName, key, self.bufferSize)
            self.delete_txt()
            return True
        except Exception as e:
            self.show_error(str(e))
            return False

    def decrypt(self, key: str) -> bool:
        try:
            pyAesCrypt.decryptFile(self.encryptetFileName, self.fileName, key, self.bufferSize)
            return True
        except ValueError:
            self.show_status("Forkert adgangskode blev angivet", False)
            return False
        except Exception as e:
            self.show_error(str(e))
            return False

    def write_text(self):
        with open(self.fileName, "w") as f:
            f.write(dpg.get_value(self.rwfield))
        password = dpg.get_value(self.writePW)
        if self.encrypt(password):
            self.show_status("Text succesfult krypteret og gemt", True)
        dpg.set_value(self.writePW, "")
        dpg.hide_item(self.writeWindow)

    def read_text(self):
        password = dpg.get_value(self.readPW)
        if self.decrypt(password):
            with open(self.fileName, "r") as f:
                dpg.set_value(self.rwfield, f.read())
            self.delete_txt()
            self.show_status("Fil dekrypteret succesfult!", True)
        dpg.set_value(self.readPW, "")
        dpg.hide_item(self.readWindow)


if __name__ == '__main__':
    w = WordSaver()

    dpg.set_primary_window(w.mainWindow, True)
    dpg.start_dearpygui()
