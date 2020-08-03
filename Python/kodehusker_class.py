#ORDHUSKER 3000

import os
import pyAesCrypt

os.system('mode con: cols=47 lines=20')


class wordSaver:
    bufferSize = 64 * 1024
    def __init__(self, fileName):
        if fileName[-4:] == ".txt":
            self.fileName = fileName
        else:
            self.fileName = fileName + ".txt"
        self.encryptetFileName = self.fileName + ".aes"
    def error(self, error):
      print(f"\nDer skete en fejl, prøv igen:\n{error}")
    def changeFileName(self):
        os.system("cls")
        self.fileName = input("""
                       Ordhusker 3000
                      Indtast filnavn: """)
        return f"Successfully changed filename to {self.fileName}"
    def emptyFile(self):
        fil = open(self.fileName, "w")
        fil.write("")
        fil.close()
    def encrypt(self, key):
        try:
            pyAesCrypt.encryptFile(self.fileName, self.encryptetFileName, key, bufferSize)
            self.emptyFile()
        except:
            return error(raise)

    def decrypt(self, key):
      try:
          pyAesCrypt.decryptFile(self.encryptetFileName, self.fileName, key, bufferSize)
      except something:
          return "Forkert Kode!"
      except:
          error(raise)






file = "john.txt"

cryptetFile = file + ".aes"



def cryptFile(mode, key):
    bufferSize = 64 * 1024
    try:
        if mode == "en":
            pyAesCrypt.encryptFile(file, cryptetFile, key, bufferSize)
            emptyFile()
            return "Kryptering Succesfuld"
        elif mode == "de":
            pyAesCrypt.decryptFile(cryptetFile, file, key, bufferSize)
            return "Dekryptering Succesfuld"
        else:
            return "ugyldig mode"
    except:
        return "Fejl"

def write():
    try:
        confirm = input("\nEr du sikker, alt gemt bliver slettet (j/n): ")
        if confirm.lower() == "j":
            text = input("\nHvad vil du skrive?: ")
            password = input("\nHvad skal koden være?: ")
            fil = open(file, "w")
            fil.write(text)
            fil.close()
            print("\n" + cryptFile("en", password))
            print("Ord gemt")
            input("\nTryk enter for hovedmenu")
        elif confirm.lower() == "n":
            print("Annuleret")
        else:
            print("Ugyldigt")
            return write()
    except:
        print("Der skete en fejl")

def read():
    count = 0
    while count<3:
        try:
            password = input("\nHvad er koden?: ")
            if password.lower() == "q":
                return
            else:
                print("\n" + cryptFile("de", password))
                fil = open(file, "r")
                print("\nDit ord er: " + str(fil.read()))
                fil.close()
                emptyFile()
                count = 3
                input("\nTryk enter for hovedmenu")
        except FileNotFoundError:
            print("Forkert Kode")
        except:
            print("Der skete en fejl")
            raise
        count+=1

fileName = input("""
                Ordhusker 3000
               Indtast filnavn: """)

word = wordSaver(fileName)

while True:
    os.system("cls")
    user = input("""
                Ordhusker 3000
    (S)kriv, (l)æs, (f)ilnavn eller (q)uit: """)
    if user.lower() == "s":
        write()
    elif user.lower() == "l":
        read()
    elif user.lower() == "f":
        word.changeFileName()
    elif user.lower() == "q":
        os.system("cls")
        break
    else:
        print("Det er ugyldigt")