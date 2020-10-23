from molmass import Formula
import re
from sympy import Matrix, lcm

elementList = []
elementMatrix = []
print("Indsæt reaktanter, husk store og små bogstaver og ingen koefficienter.")
reactants = input("Reaktanter: ")
print("Indsæt Produkter, husk store og små bogstaver og ingen koefficienter.")
products = input("Produkter: ")
reactants = reactants.replace(' ', '').split("+")
products = products.replace(' ', '').split("+")

substances = reactants + products
molMass = [Formula(x).mass for x in substances]

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

print(substances, coEffiList, molMass, output, sep="\n")

knownMassIndex = input("Indsæt index værdi af stoffet med en kendt masse: ")
knownMassIndex = int(knownMassIndex)
knownMass = input(f"Hvad er massen af {substances[knownMassIndex]} i gram?: ")
knownMass = float(knownMass)

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

print("", substances, coEffiList, n, molMass, massList, sep="\n")
