from random import randint

def jasm(boolean):
    x = randint(0, 50)
    if x == 9:
        return boolean
    print(x)
    return "Måske"

x = True

gange = 0

while True:

    gange += 1