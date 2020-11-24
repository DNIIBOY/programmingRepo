from rich import *
from rich.table import Table
from rich.console import Console
from rich import pretty
from molmass import Formula
import re
from sympy import Matrix, lcm
import os
import sys
import xlwt
from tempfile import TemporaryFile

fileName = "kemi.xls"
os.system('mode con: cols=80 lines=15')
pretty.install()
console = Console()


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


def balance(productsSym, molMass, substances):
    global console
    console.print("Skal reaktionsskemaet automatisk afstemmes? ([green]j[/green]/[red]n[/red]): ", end="")
    autoBalance = input()
    if autoBalance.lower() == "j":
        global elementMatrix
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
        return [coEffi[i][0] for i in range(len(reactants))] + [coEffi[i + len(reactants)][0] for i in range(len(products))]
    elif autoBalance.lower() == "n":
        console.clear()
        x = Table(show_header=True, header_style="cyan")
        x.add_column("Af: Daniel Nettelfield")
        for i in productsSym:
            x.add_column(i)
        x.add_row(*(["Molare Masse [g/mol]"] + [str(round(i, 4)) for i in molMass]))
        x.add_row(*(["Index Værdi"] + [str(i + 1) for i in range(len(substances))]))
        console.print(x)
        return [int(input(f"Indsæt koefficient {i}: ")) for i in range(1, len(substances) + 1)]
    elif autoBalance.lower() == "q":
        console.clear()
        sys.exit()
    else:
        console.print("Ugyldigt input")
        return balance(productsSym, molMass, substances)


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
    console.clear()
    try:
        elementList = []
        elementMatrix = []
        console.print("Indsæt reaktanter, husk store og små bogstaver og ingen koefficienter.", "[blue]Reaktanter: [/blue]", end="")
        reactants = input()
        if reactants == "c":
            continue
        elif reactants == "q":
            console.clear()
            sys.exit()
        console.print("Indsæt Produkter, husk store og små bogstaver og ingen koefficienter.", "[blue]Produkter: [/blue]", end="")
        products = input()
        if products == "c":
            continue
        elif products == "q":
            console.clear()
            sys.exit()
        reactants = reactants.replace(' ', '').split("+")
        products = products.replace(' ', '').split("+")
        productsSym = ["+ "+i if reactants.index(i) != 0 else i for i in reactants] + ["+ "+x if products.index(x) != 0 else "-> " + x for x in products]

        substances = reactants + products
        molMass = [Formula(x).mass for x in substances]

        coEffiList = balance(productsSym, molMass, substances)

        x = Table(show_header=True, header_style="cyan")
        x.add_column("Af: Daniel Nettelfield")
        for i in productsSym:
            x.add_column(i)
        x.add_row(*(["Koefficient"] + [str(i) for i in coEffiList]))
        x.add_row(*(["Molare Masse [g/mol]"] + [str(round(i, 4)) for i in molMass]))
        x.add_row(*(["Index Værdi"] + [str(i+1) for i in range(len(substances))]))

        console.clear()
        console.print(x)

        knownMassIndex = input("Indsæt index værdi af stoffet med en kendt masse: ")
        if knownMassIndex == "c":
            continue
        elif knownMassIndex == "q":
            console.clear()
            sys.exit()
        knownMassIndex = int(knownMassIndex) - 1
        knownMass = input(f"Hvad er massen af {substances[knownMassIndex]} i gram?: ")
        if knownMass == "c":
            continue
        if knownMass == "q":
            console.clear()
            sys.exit()
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

        x = Table(show_header=True, header_style="cyan")
        x.add_column("Af: Daniel Nettelfield")
        for i in productsSym:
            x.add_column(i)
        x.add_row(*(["Koefficient"] + [str(i) for i in coEffiList]))
        x.add_row(*(["Stofmængde [mol]"] + [str(round(i, 4)) for i in n]))
        x.add_row(*(["Molare Masse [g/mol]"] + [str(round(i, 4)) for i in molMass]))
        x.add_row(*(["Masse [g]"] + [str(round(i, 4)) for i in massList]))

        console.clear()
        console.print(x)

        option = input("\nTryk enter for at starte igen")
        if option.lower() == "q":
            console.clear()
            sys.exit()
        elif option.lower() == "e":
            book = xlwt.Workbook()
            sheet = book.add_sheet("Daniels Ting")
            kol1 = ["Af: Daniel Nettelfield", "Koefficient", "Stofmængde [mol]", "Molare Masse [g/mol]", "Masse [g]"]
            for i, e in enumerate(kol1):
                sheet.write(i, 0, e)
            print(productsSym, coEffiList, n, molMass, massList)
            for x in productsSym:
                y = productsSym.index(x)
                z = [x, coEffiList[y], [round(i, 4) for i in n][y], [round(i, 4) for i in molMass][y], [round(i, 4) for i in massList][y]]
                print(z)
                for i, e in enumerate(z):
                    sheet.write(i, y+1, e)

            book.save(fileName)
            book.save(TemporaryFile())

    except Exception as e:
        raise
        console.print(f"Der skete en fejl", 2*"\n", e, "\n")
        input("Tryk enter for at prøve igen")
