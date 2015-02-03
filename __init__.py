__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uWatermarkWidget import UWatermarkWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uWatermarkWidget = UWatermarkWidget()
    uWatermarkWidget.show()
    app.exec_()