import random

while True:
    guess = ""
    num = random.randint(1, 100)
    numsq = num**2
    while guess != num:
        try:
            guess = int(input(f"What is square root of {numsq}?: "))
        except ValueError:
            print("Must be integer!")
            continue
        if guess != num:
            print("Incorrect")
    print("Correct")
