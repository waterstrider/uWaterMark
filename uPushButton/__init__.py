__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uPushButton.uPushButton import UPushButton


if __name__ == "__main__":
    app = QApplication(argv)
    uPushButton = UPushButton()
    uPushButton.show()
    app.exec_()