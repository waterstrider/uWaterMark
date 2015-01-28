__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uImageViewer.uImageViewer import UImageViewer


if __name__ == "__main__":
    app = QApplication(argv)
    uImageViewer = UImageViewer()
    uImageViewer.show()
    app.exec_()