__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uWatermark import UWatermark


if __name__ == "__main__":
    app = QApplication(argv)
    uWatermark = UWatermark()
    uWatermark.show()
    app.exec_()