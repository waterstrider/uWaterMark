__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uSourceImage.uSourceImageWidget import USourceImageWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uSourceImageWidget = USourceImageWidget()
    uSourceImageWidget.show()
    app.exec_()