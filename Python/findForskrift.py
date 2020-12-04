import os
while True:
    os.system("cls")
    try:
        x1, y1, x2, y2, = int(input("Hvad er x1?: ")), int(input("Hvad er y1?: ")), int(input("Hvad er x2?: ")), int(input("Hvad er y2?: "))
        a = (y1 - y2)/(x1 - x2)
        b = y1-a*x1
    except Exception as e:
        print("\n", e, "\n")
        input("Tryk enter for at prøve igen")
        continue

    print(f"""
a = ({y1} - {y2})/({x1} - {x2}) = {a}
b = {y1} - {a} * {x1} = {b}

f(x) = {a}x{"+"*(b>0)}{b}""")
    input("\nTryk enter for reset")