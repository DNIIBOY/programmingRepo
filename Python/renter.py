from os import system
from math import log
streg = "-------------------------------------"


def main(mode):
    if mode == "kn":
        slutkapital()
    elif mode == "k" or mode == "k0":
        startkapital()
    elif mode == "r":
        rente()
    elif mode == "n":
        terminer()
    else:
        print("Ugyldigt input")

    input("Tryk enter for at fortsætte")


def slutkapital():
    k = float(input("Hvad er startværdien?: "))
    rp = float(input("Hvad er renten i procent?: "))
    r = rp / 100
    n = float(input("Hvor mange terminer?: "))
    kn = k * (1 + r) ** n
    kn = round(kn, 2)
    system("cls")
    print("Kn er: " + str(kn))
    print(f"Kn = {k} * (1 + {r})^{n} = {kn}")


def startkapital():
    kn = float(input("Hvad er slutværdien?: "))
    rp = float(input("Hvad er renten i procent?: "))
    r = rp / 100
    n = float(input("Hvor mange terminer?: "))
    k = (kn / (1 + r) ** n)
    system("cls")
    k = round(k, 2)
    print("K er: " + str(k))
    print(f"K = {kn} / (1 + {r})^{n} = {k}")


def rente():
    k = float(input("Hvad er startværdien?: "))
    kn = float(input("Hvad er slutværdien?: "))
    n = float(input("Hvor mange terminer?: "))
    r = ((kn/k)-1)**1/n
    system("cls")
    r = round(r, 2)
    print("R er: " + str(r))
    print(f"R = {n}√(({kn}/{k}))-1 = {r}")


def terminer():
    k = float(input("Hvad er startværdien?: "))
    kn = float(input("Hvad er slutværdien?: "))
    r = float(input("Hvad er renten?: "))
    n = log(kn/k)/log(1+r)
    system("cls")
    n = round(n, 2)
    print("N er: ", str(n))
    print(f"N = log({kn} / {k}) / log(1 + {r})")


while True:
    system("cls")
    print("""---------Dannis Rentemaskine--------
         Kn = K0 * (1 + R)^N""")
    mode = input("Mangler du Kn, K, R, eller N?: ")
    mode = mode.lower()
    main(mode)
