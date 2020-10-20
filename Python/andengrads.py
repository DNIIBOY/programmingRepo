from math import sqrt
import os

os.system('mode con: cols=42 lines=20')


def andengrad(a, b, c, mellem):
    diskrimi = 0
    r1 = 0
    r2 = 0
    topx = 0
    topy = 0
    try:
        diskrimi = (b * b) - (4 * a * c)
        kvdiskrimi = sqrt(diskrimi)
        r1 = (0 - b - kvdiskrimi) / (2 * a)
        r2 = (0 - b + kvdiskrimi) / (2 * a)
        topx = (0 - b) / (2 * a)
        topy = 0 - diskrimi / (4 * a)
    except:
        print("Der er ingen løsninger")
        try:
            topx = (0 - b) / (2 * a)
            topy = 0 - diskrimi / (4 * a)
        except:
            pass

    if mellem.lower() == "n":
        print("Diskriminant: " + str(diskrimi))
        print("Toppunkt: " + str(round(topx, 2)) + ", " + str(round(topy, 2)))
        print("Rod 1: " + str(round(r1, 2)))
        print("Rod 2: " + str(round(r2, 2)))

    elif mellem.lower() == "j":
        a = round(a, 4)
        b = round(b, 4)
        c = round(c, 4)
        print(f"""Diskriminant:
{b}² - (4 * {a} * {c}) = {round(diskrimi, 4)}""")
        print(f"""Rødder:
(-{b} + √({round(diskrimi, 4)}) / 2 * {a} = {round(r2, 4)}
(-{b} - √({round(diskrimi, 4)}) / 2 * {a} = {round(r1, 4)}""")
        print(f"""Toppunkt:
x = -{b} / 2 * {a} = {round(topx, 4)}
y = -{round(diskrimi, 4)} / 4 * {a} = {round(topy, 4)}""")
        print("""-----------------------------------------""")


def fixfloat(num):
    if "," in num:
        num = [x for x in num]
        for i in num:
            if i == ",":
                value = num.index(i)
                num.pop(value)
                num.insert(value, ".")
        num = float("".join(num))
    else:
        num = eval(num)
    return float(num)


while True:
    print("""----------Andengrads Funktioner----------
         Af: Daniel Nettelfield""")
    try:
        a = input("""            Indsæt a værdi: """)
        if a.lower() == "q":
            break
        elif a.lower() == "c":
            os.system("cls")
            continue
        else:
            a = fixfloat(a)
        b = input("""            Indsæt b værdi: """)
        if b.lower() == "q":
            break
        elif b.lower() == "c":
            os.system("cls")
            continue
        else:
            b = fixfloat(b)
        c = input("""            Indsæt c værdi: """)
        if c.lower() == "q":
            break
        elif c.lower() == "c":
            os.system("cls")
            continue
        else:
            c = fixfloat(c)
        mellem = str(input("""Vil du have mellemregninger med? (j/n): """))
        print("------------------------------------------")
        if mellem.lower() == "j" or mellem.lower() == "n":
            andengrad(a, b, c, mellem)
        elif mellem.lower() == "q":
            break
        elif mellem.lower() == "c":
            os.system("cls")
            continue
        else:
            print("Ugyldigt Input")
    except:
        print("""            Ugyldigt Input""")
