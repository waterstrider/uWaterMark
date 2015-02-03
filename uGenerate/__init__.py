__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uGenerate.uGenerate import UGenerate


if __name__ == "__main__":
    app = QApplication(argv)
    uGenerate = UGenerate()
    uGenerate.show()
    app.exec_()