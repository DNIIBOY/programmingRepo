import os

while True:
    os.system("cls")
    længde, bredde, højde, dybde, densitet = float(input("Længde[m]: ")), float(input("Bredde[m]: ")), float(input("Højde[m]: ")), float(input("Oversidens dybde[m]: ")), float(input("Vandets densitet[kg/m3]: "))

    areal = bredde*længde #m2
    trykTop = densitet*dybde*9.82 #Pa
    kraftTop = trykTop*areal #N

    trykBund = densitet*(dybde+højde)*9.82 #Pa
    kraftBund = trykBund*areal #N

    opdrift = kraftBund-kraftTop #N

    udregn = input("Udregninger?: (j/n): ").lower()

    if udregn == "n":
        print(f"""
        Areal: {areal} m2
        Trykket på oversiden: {trykTop}Pa
        Kraften på oversiden: {kraftTop}N
        Trykket på bunden: {trykBund}Pa
        Kraften på bunden: {kraftBund}N
        Opdriften er {opdrift}N""")
    elif udregn == "j":
        print(f"""
            Areal: {længde}m * {bredde}m = {areal} m2
            Trykket på oversiden: {densitet}kg/m3 * {dybde}m * 9.82 = {trykTop}Pa
            Kraften på oversiden: {trykTop}Pa * {areal}m2 = {kraftTop}N
            Trykket på bunden: {densitet}kg/m3 *({dybde}m+2m) = {trykBund}Pa
            Kraften på bunden: {trykBund}Pa * {areal}m2 = {kraftBund}N
            Opdrift: {kraftBund}N - {kraftTop}N = {opdrift}N""")
    else:
        continue
    input()