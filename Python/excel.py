import xlwt
from tempfile import TemporaryFile

book = xlwt.Workbook()
sheet = book.add_sheet("Daniels Ting")

kol1 = ["Af: Daniel Nettelfield", "Koefficient", "Stofmængde [mol]", "Molare Masse [g/mol]", "Masse [g]"]

productsSym = ['H2', '+ Cl2', '-> HCl']
coEffiList = [1, 1, 2]
n = [1.68674112591095, 1.68674112591095, 3.3734822518218928]
molMass = [2.015882, 70.9058, 36.460841]
massList = [3.40027107438361, 119.599728925616, 123.0]

for i, e in enumerate(kol1):
    sheet.write(i, 0, e)
for x in productsSym:
    y = productsSym.index(x)
    z = [x, coEffiList[y], [round(i, 4) for i in n][y], [round(i, 4) for i in molMass][y], [round(i, 4) for i in massList][y]]
    for i, e in enumerate(z):
        sheet.write(i, y+1, e)

name = "kemi.xls"
book.save(name)
book.save(TemporaryFile())
