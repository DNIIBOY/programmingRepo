import os
import pyAesCrypt

# ORDHUSKER 3000

file = "john.txt"

cryptetFile = file + ".aes"

os.system('mode con: cols=47 lines=20')


def empty_file():
    fil = open(file, "w")
    fil.write("")
    fil.close()


def crypt_file(mode, key):
    bufferSize = 64 * 1024
    try:
        if mode == "en":
            pyAesCrypt.encryptFile(file, cryptetFile, key, bufferSize)
            empty_file()
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
            print("\n" + crypt_file("en", password))
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
    while count < 3:
        try:
            password = input("\ er koden?: ")
            if password.lower() == "q":
                return
            else:
                print("\n" + crypt_file("de", password))
                fil = open(file, "r")
                print("\nDit ord er: " + str(fil.read()))
                fil.close()
                empty_file()
                count = 3
                input("\nTryk enter for hovedmenu")
        except FileNotFoundError:
            print("Forkert Kode")
        except:
            print("Der skete en fejl")
            raise
        count += 1


while True:
    os.system("cls")
    user = input("""
                Ordhusker 3000
        (S)kriv, (l)æs eller (q)uit: """)
    if user.lower() == "s":
        write()
    elif user.lower() == "l":
        read()
    elif user.lower() == "q":
        os.system("cls")
        break
    else:
        print("Det er ugyldigt")
