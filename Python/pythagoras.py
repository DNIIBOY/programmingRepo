from math import sqrt
def pythagoras(a=0, b=0, c=0):
    if a == 0 and b != 0 and c!= 0:
        print("A = " + str(sqrt(c*c - b*b)))
    elif b == 0 and a != 0 and c != 0:
        print("B = " + str(sqrt(c*c - a*a)))
    elif c == 0 and a != 0 and b != 0:
        print("C = " + str(sqrt(a*a + b*b)))
    else:
        print("Der er sket en fejl")

while True:
    print("""------------Pythagoras-------------
        Skriv 0 for ukendt""")
    a = int(input("Indsæt a: "))
    b = int(input("Indsæt b: "))
    c = int(input("Indsæt c: "))
    pythagoras(a, b, c)