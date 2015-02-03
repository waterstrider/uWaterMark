__author__ = 'Shiraga-P'

from sys import argv

from PySide.QtGui import QApplication

from uImagesList.uImagesListWidget import UImagesListWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uImagesListWidget = UImagesListWidget()
    uImagesListWidget.show()
    app.exec_()