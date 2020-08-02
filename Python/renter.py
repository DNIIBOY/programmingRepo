streg = "-------------------------------------"

def rente(mode):
    if mode == "kn":
        k = float(input("Hvad er startværdien?: "))
        rp = float(input("Hvad er renten i procent?: "))
        r = rp/100
        n = float(input("Hvor mange terminer?: "))
        kn = k * (1+r)**n
        print(streg)
        print("Kn er: " + str(round(kn, 2)))
    elif mode == "k":
        kn = float(input("Hvad er slutværdien?: "))
        rp = float(input("Hvad er renten i procent?: "))
        r = rp / 100
        n = float(input("Hvor mange terminer?: "))
        k = (kn/(1+r)**n)
        print(streg)
        print("K er: " + str(round(k, 2)))

while True:
    print("---------Dannis Rentemaskine--------")
    mode = input("Mangler du Kn, K, R, eller N?: ")
    mode = mode.lower()
    rente(mode)