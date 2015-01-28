__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uDestination.uDestination import UDestination


if __name__ == "__main__":
    app = QApplication(argv)
    uDestination = UDestination()
    uDestination.show()
    app.exec_()