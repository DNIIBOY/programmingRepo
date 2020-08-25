while True:
    n1 = input("s eller l: ")
    if n1 == "s".lower():
        hyggen = input("Skriv noget: ")
    elif n1 =="l".lower():
        print(hyggen)
    else:
        print("Wtf")