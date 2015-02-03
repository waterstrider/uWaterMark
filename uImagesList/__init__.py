__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uImagesList.uImagesList import UImagesList


if __name__ == "__main__":
    app = QApplication(argv)
    uImagesList = UImagesList()
    uImagseList.show()
    app.exec_()