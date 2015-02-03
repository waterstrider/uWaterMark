__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uPosition.uPositionWidget import UPositionWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uPositionWidget = UPositionWidget()
    uPositionWidget.show()
    app.exec_()