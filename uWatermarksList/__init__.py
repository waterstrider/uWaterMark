__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uWatermarksList.uWatermarksList import UWatermarksList


if __name__ == "__main__":
    app = QApplication(argv)
    uWatermarksList = UWatermarksList()
    uWatermarksList.show()
    app.exec_()