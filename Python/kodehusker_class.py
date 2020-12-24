# ORDHUSKER 3000

from time import sleep
from sys import exit
import os
import pyAesCrypt

# Set pause time between actions (in seconds):
sleeptime = 2

os.system('mode con: cols=47 lines=20')


class WordSaver:

    # Set buffersize for encryption and decryption
    bufferSize = 64 * 1024

    # Create static method for displaying error messages
    @staticmethod
    def error(error):
        return f"\nDer skete en fejl, prøv igen:\n{error}"
        
    # Method for qutting the program and going back to normal terminal
    @staticmethod
    def quit():
        os.system('mode con: cols=80 lines=20')
        os.system("cls")
        exit()

    # Initiate the object with a filename and automate creating the filename for the encrypted file
    def __init__(self, filename):
        if filename[-4:] == ".txt":
            self.fileName = filename
        else:
            self.fileName = filename + ".txt"
        self.encryptetFileName = self.fileName + ".aes"

    # Function for changing the filename of the object
    def changefilename(self):
        os.system("cls")
        filename = input("""
              Ordhusker 3000
             Indtast filnavn: """)
        if filename[-4:] == ".txt":
            self.fileName = filename
        else:
            self.fileName = filename + ".txt"
        self.encryptetFileName = self.fileName + ".aes"
        return f"Skiftede filnavn til {self.fileName}"

    # Function for emptying the file with the filename of the object
    def emptyfile(self):
        os.remove(self.fileName)

    # Encrypt the file using the key entered by the user in the write() function
    def encrypt(self, key):
        try:
            pyAesCrypt.encryptFile(self.fileName, self.encryptetFileName, key, self.bufferSize)
            self.emptyfile()
            return "Kryptering Successfuld"
        except Exception as e:
            return WordSaver.error(str(e))

    # Decrypt the file using the key entered by the user in the read() function.
    # Use ValueError to detect wrong password
    def decrypt(self, key):
        try:
            pyAesCrypt.decryptFile(self.encryptetFileName, self.fileName, key, self.bufferSize)
            return "Dekrypering Successfuld"
        except ValueError:
            return "Forkert Kode!"
        except Exception as e:
            return WordSaver.error(str(e))

    # Function for writing to the file. Writes to .txt file and calls encrypt() function
    # to encrypt. encrypt() then calls emptyfile() to remove any raw text from .txt file
    def write(self):
        try:
            confirm = input("\nEr du sikker, alt gemt bliver slettet (j/n): ")
            if confirm.lower() == "j":
                text = input("\nHvad vil du skrive?: ")
                password = input("\nHvad skal koden være?: ")
                fil = open(self.fileName, "w")
                fil.write(text)
                fil.close()
                print("\n" + self.encrypt(password))
                print("Ord gemt")
                input("\nTryk enter for hovedmenu")
                return "..."
            elif confirm.lower() == "n":
                return "Annulleret"
            else:
                print("Ugyldigt")
                return self.write()
        except Exception as e:
            return WordSaver.error(str(e))

    # Function for reading the aes file. Calls decrypt() with user entered key for decryption
    def read(self):
        count = 0
        while count < 3:
            try:
                password = input("\nHvad er koden?: ")
                if password.lower() == "q":
                    return "Quitting read mode"
                else:
                    print("\n" + self.decrypt(password) + "\n")
                    fil = open(self.fileName, "r")
                    print("-" * 30)
                    print("Dit ord er: " + str(fil.read()))
                    print("-" * 30)
                    fil.close()
                    self.emptyfile()
                    count = 3
                    input("\nTryk enter for hovedmenu")
                    return "..."
            except FileNotFoundError:
                pass
            except Exception as e:
                return WordSaver.error(str(e))
            count += 1
        return "For mange forsøg"

    # Main function, calls all other functions to run the program.
    def run(self):
        global sleeptime
        while True:
            os.system("cls")
            user = input(f"""
              Filnavn: {self.fileName}

               Ordhusker 3000
   (S)kriv, (l)æs, (f)ilnavn eller (q)uit: """)
            if user.lower() == "s":
                print(self.write())
                sleep(sleeptime)
            elif user.lower() == "l":
                print(self.read())
                sleep(sleeptime)
            elif user.lower() == "f":
                print(self.changefilename())
                sleep(sleeptime)
            elif user.lower() == "q":
                WordSaver.quit()
            else:
                print("Ugyldigt input")
                sleep(sleeptime)


# Starts the program, uses user input filename to create WordSaver object.
# Only runs if program is run as script.
if __name__ == '__main__':
    fileName = input("""
               Ordhusker 3000
              Indtast filnavn: """)
    word = WordSaver(fileName)
    word.run()
