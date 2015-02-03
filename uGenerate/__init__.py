__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uGenerate.uGenerateWidget import UGenerateWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uGenerate = UGenerateWidget()
    uGenerateWidget.show()
    app.exec_()