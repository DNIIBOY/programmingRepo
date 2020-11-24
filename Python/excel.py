import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet("Daniels Ting")

supersecretdata = ["hyggenygge", 123, "mojn", 69, 420]
line2 = ["gamer", 12345, "hejsa"]

for i,e in enumerate(supersecretdata):
    sheet1.write(i,0,e)

for i,e in enumerate(line2):
    sheet1.write(i,1,e)

name = "kemi.xls"
book.save(name)
book.save(TemporaryFile())
