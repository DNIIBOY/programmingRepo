import os
while True:
    os.system("cls")
    print("   ___                        __   __       ____                          __   ")
    print("  |__ \    ____  __  ______  / /__/ /______/ __/___  _________ ___  ___  / /  ")
    print("  __/ /   / __ \/ / / / __ \/ //_/ __/ ___/ /_/ __ \/ ___/ __ `__ \/ _ \/ /  ")
    print(" / __/   / /_/ / /_/ / / / / ,< / /_(__  ) __/ /_/ / /  / / / / / /  __/ /  ")
    print("/____/  / .___/\__,_/_/ /_/_/|_|\__/____/_/  \____/_/  /_/ /_/ /_/\___/_/  ")
    print("       /_/                                                                ")

    try:
        x1, y1, x2, y2, = float(input("Hvad er x1?: ")), float(input("Hvad er y1?: ")), float(input("Hvad er x2?: ")), float(input("Hvad er y2?: "))
        a = (y1 - y2)/(x1 - x2)
        b = y1-a*x1
    except Exception as e:
        print("\n", e, "\n")
        input("Tryk enter for at prøve igen")
        continue
    y1, y2, x1, x2, a, b, = [round(i, 4) for i in [y1, y2, x1, x2, a, b]]

    print(f"""
a = ({y1} - {y2})/({x1} - {x2}) = {a}
b = {y1} - {a} * {x1} = {b}

f(x) = {a}x{"+"*(b>0)}{b}""")
    input("\nTryk enter for reset")
