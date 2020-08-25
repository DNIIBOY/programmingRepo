#ORDHUSKER 3000
text = "Der er ikke noget ord gemt"
def write():
    try:
        koode = open("ikkeEnKode.txt", "r")
        if input("Hvad er koden?: ") == koode.read():
            koode.close()
            text = input("Hvad vil du gemme?: ")
            fil = open("john.txt", "w")
            fil.write(text)
            fil.close()
            print("Ord gemt")
    except:
        print("Der skete en fejl")

def read():
    try:
        koode = open("ikkeEnKode.txt", "r")
        if input("Hvad er koden?: ") == koode.read():
            koode.close()
            fil = open("john.txt", "r")
            print("Dit ord er: " + str(fil.read()))
    except:
        print("Der skete en fejl")

def koden():
    try:
        koode = open("ikkeEnKode.txt", "r")
        if input("Hvad er koden?: ") == koode.read():
            koode.close()
            koode = open("ikkeEnKode.txt", "w")
            nykode = input("Hvad skal den nye kode være?: ")
            koode.write(nykode)
        else:
            print("Forkert")
    except:
        print("Der skete en fejl")

while True:
    user = input("""
    (S)kriv, (l)æs, (k)ode eller (q)uit: """)
    if user == "s".lower():
        write()
    elif user == "l".lower():
        read()
    elif user == "k".lower():
        koden()
    elif user == "q".lower():
        break
    else:
        print("Det er ugyldigt")