from molmass import Formula
import re
from sympy import Matrix, lcm
from prettytable import PrettyTable
import os

os.system('mode con: cols=100 lines=10')

def addToMatrix(element, index, count, side):
    if index == len(elementMatrix):
        elementMatrix.append([])
        for _ in elementList:
            elementMatrix[index].append(0)
    if element not in elementList:
        elementList.append(element)
        for i in range(len(elementMatrix)):
            elementMatrix[i].append(0)
    column = elementList.index(element)
    elementMatrix[index][column] += count * side


def findElements(segment, index, multiplier, side):
    elementsAndNumbers = re.split('([A-Z][a-z]?)', segment)
    i = 0
    while i < len(elementsAndNumbers) - 1:
        i += 1
        if len(elementsAndNumbers[i]) > 0:
            if elementsAndNumbers[i + 1].isdigit():
                count = int(elementsAndNumbers[i + 1]) * multiplier
                addToMatrix(elementsAndNumbers[i], index, count, side)
                i += 1
            else:
                addToMatrix(elementsAndNumbers[i], index, multiplier, side)


def compoundDecipher(compound, index, side):
    segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
    for segment in segments:
        if segment.startswith("("):
            segment = re.split('\)([0-9]*)', segment)
            multiplier = int(segment[1])
            segment = segment[0][1:]
        else:
            multiplier = 1
        findElements(segment, index, multiplier, side)


def fixfloat(num):
    if "," in num:
        num = [x for x in num]
        for i in num:
            if i == ",":
                value = num.index(i)
                num.pop(value)
                num.insert(value, ".")
        num = float("".join(num))
    else:
        num = eval(num)
    return float(num)


while True:
    os.system("cls")
    try:
        elementList = []
        elementMatrix = []
        print("Indsæt reaktanter, husk store og små bogstaver og ingen koefficienter.")
        reactants = input("Reaktanter: ")
        if reactants == "c":
            continue
        elif reactants == "q":
            quit()
        print("Indsæt Produkter, husk store og små bogstaver og ingen koefficienter.")
        products = input("Produkter: ")
        if products == "c":
            continue
        elif products == "q":
            quit()
        reactants = reactants.replace(' ', '').split("+")
        products = products.replace(' ', '').split("+")
        productsSym = ["+ "+i if reactants.index(i) != 0 else i for i in reactants ] + ["+ "+x if products.index(x) != 0 else "-> " + x for x in products]

        substances = reactants + products
        molMass = [Formula(x).mass for x in substances]

        for i in range(len(reactants)):
            compoundDecipher(reactants[i], i, 1)
        for i in range(len(products)):
            compoundDecipher(products[i], i + len(reactants), -1)
        elementMatrix = Matrix(elementMatrix)
        elementMatrix = elementMatrix.transpose()
        solution = elementMatrix.nullspace()[0]
        multiple = lcm([val.q for val in solution])
        solution = multiple * solution
        coEffi = solution.tolist()
        output = ""
        coEffiList = []
        for i in range(len(reactants)):
            output += str(coEffi[i][0]) + reactants[i]
            if i < len(reactants) - 1:
                output += " + "
            coEffiList.append(coEffi[i][0])
        output += " -> "
        for i in range(len(products)):
            output += str(coEffi[i + len(reactants)][0]) + products[i]
            if i < len(products) - 1:
                output += " + "
            coEffiList.append(coEffi[i + len(reactants)][0])

        x = PrettyTable()
        x.field_names = ["Af: Daniel Nettelfield"] + productsSym
        x.add_row(["Koefficient"] + [str(i) for i in coEffiList])
        x.add_row(["Molare Masse [g/mol]"] + [str(round(i, 4)) for i in molMass])
        x.add_row(["Index Værdi"] + [str(i+1) for i in range(len(substances))])

        os.system("cls")
        print(x)

        knownMassIndex = input("Indsæt index værdi af stoffet med en kendt masse: ")
        if knownMassIndex == "c":
            continue
        elif knownMassIndex == "q":
            quit()
        knownMassIndex = int(knownMassIndex) - 1
        knownMass = input(f"Hvad er massen af {substances[knownMassIndex]} i gram?: ")
        if knownMass == "c":
            continue
        if knownMass == "q":
            quit()
        knownMass = fixfloat(knownMass)

        oneKnownMol = knownMass / molMass[knownMassIndex] / coEffiList[knownMassIndex]

        calcSub = substances.pop(knownMassIndex)
        calcCoEffi = coEffiList.pop(knownMassIndex)
        calcMolMass = molMass.pop(knownMassIndex)

        n = [sub*oneKnownMol for sub in coEffiList]
        massList = [n[i]*molMass[i] for i in range(len(substances))]

        substances.insert(knownMassIndex, calcSub)
        coEffiList.insert(knownMassIndex, calcCoEffi)
        molMass.insert(knownMassIndex, calcMolMass)
        massList.insert(knownMassIndex, knownMass)
        n.insert(knownMassIndex, knownMass / molMass[knownMassIndex])

        x.clear_rows()
        x.add_row(["Koefficient"] + [str(i) for i in coEffiList])
        x.add_row(["Stofmængde [mol]"] + [str(round(i, 4)) for i in n])
        x.add_row(["Molare Masse [g/mol]"] + [str(round(i, 4)) for i in molMass])
        x.add_row(["Masse [g]"] + [str(round(i, 4)) for i in massList])

        os.system("cls")
        print(x)

        if input("\nTryk enter for at starte igen") == "q":
            quit()

    except Exception as e:
        print(f"Der skete en fejl", 2*"\n", e, "\n")
        input("Tryk enter for at prøve igen")