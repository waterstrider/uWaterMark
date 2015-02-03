__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uDestination.uDestinationWidget import UDestinationWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uDestination = UDestinationWidget()
    uDestination.show()
    app.exec_()