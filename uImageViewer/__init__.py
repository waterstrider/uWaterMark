__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uImageViewer.uImageViewerWidget import UImageViewerWidget

if __name__ == "__main__":
    app = QApplication(argv)
    uImageViewerWidget = UImageViewerWidget()
    uImageViewerWidget.show()
    app.exec_()