__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uTextWatermark.uTextWatermarkWidget import UTextWatermarkWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uTextWatermarkWidget = UTextWatermarkWidget()
    uTextWatermarkWidget.show()
    app.exec_()