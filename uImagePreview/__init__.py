__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uImagePreview.uImagePreviewWidget import UImagePreviewWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uImageViewer = UImagePreviewWidget()
    uImageViewer.show()
    app.exec_()