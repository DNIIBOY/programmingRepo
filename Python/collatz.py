from sys import exit

steps = 0

def collatz(number):
    global steps
    if number == 1:
        print(f"Hit 1 in {steps} steps\n")
        steps = 0
    elif number % 2 == 0:
        calc = number // 2
        print(calc)
        steps += 1
        return collatz(calc)
    else:
        calc = 3 * number + 1
        print(calc)
        steps += 1
        return collatz(calc)

while True:
    try:
        print("Enter Number:")
        collatz(int(input()))
    except ValueError:
        print("Only Integers")
    except KeyboardInterrupt:
        exit()
