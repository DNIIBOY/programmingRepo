from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 200, 400, 400)
    win.setWindowTitle("Kemi Mængdeberegner. Daniel Nettelfield")

    label = QtWidgets.QLabel(win)
    label.setText("Danni er en alfa")
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())


window()
