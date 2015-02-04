__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uImageWatermark.uImageWatermarkWidget import UImageWatermarkWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uImageWatermarkWidget = UImageWatermarkWidget()
    uImageWatermarkWidget.show()
    app.exec_()