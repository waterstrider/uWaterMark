__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uRotate.uRotateWidget import URotateWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uRotateWidget = URotateWidget()
    uRotateWidget.show()
    app.exec_()