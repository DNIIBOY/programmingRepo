from math import sqrt
import os

os.system('mode con: cols=42 lines=20')

def andengrad(a, b, c, mellem):
    diskrimi = 0
    r1 = 0
    r2 = 0
    topx = 0
    topy = 0
    kvdiskrimi = 0
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
        print("""Diskriminant:
{}^2 - 4 * {} * {} = {}""".format(b, a, c, round(diskrimi, 4)))
        print("""Rødder:
(-{} + sqrt({})) / 2 * {} = {}
(-{} - sqrt({})) / 2 * {} = {}""".format(b, round(diskrimi, 4), a, round(r2, 4), b, round(diskrimi, 4), a, round(r1, 4)))
        print("""Toppunkt:
x = -{} / 2 * {} = {}
y = -{} / 4 * {} = {}""".format(b, a, round(topx, 4), round(diskrimi, 4), a, round(topy, 4)))
        print("""-----------------------------------------""")


while True:
    print("""---------Andengrads Funktioner-----------""")
    try:
        a = input("""            Indsæt a værdi: """)
        if a.lower() == "q":
            break
        a = float(a)
        b = input("""            Indsæt b værdi: """)
        if b.lower() == "q":
            break
        b = float(b)
        c = input("""            Indsæt c værdi: """)
        if c.lower() == "q":
            break
        c = float(c)
        mellem = str(input("""Vil du have mellemregninger med? (j/n): """))
        print("------------------------------------------")
        if mellem.lower() == "j" or mellem.lower() == "n":
            andengrad(a, b, c, mellem)
        elif mellem.lower() =="q":
            break
        else:
            print("Ugyldigt Input")
    except:
        print("""            Ugyldigt Input""")