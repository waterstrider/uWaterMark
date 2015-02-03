__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uWatermarksList.uWatermarksListWidget import UWatermarksListWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uWatermarksList = UWatermarksListWidget()
    uWatermarksListWidget.show()
    app.exec_()