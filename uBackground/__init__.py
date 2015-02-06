__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uBackground.uBackgroundWidget import UBackgroundWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uBackgroundWidget = UBackgroundWidget()
    uBackgroundWidget.show()
    app.exec_()