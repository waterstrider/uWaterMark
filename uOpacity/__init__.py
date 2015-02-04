__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uOpacity.uOpacityWidget import UOpacityWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uOpacityWidget = UOpacityWidget()
    uOpacityWidget.show()
    app.exec_()