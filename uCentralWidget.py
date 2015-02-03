__author__ = 'waterstrider.vin'

from PySide.QtGui import *

from uWatermarksList.uWatermarksList import UWatermarksList
from uImagesList.uImagesList import UImagesList
from uGenerate.uGenerate import UGenerate
from uDestination.uDestination import UDestination
from uImageViewer.uImageViewer import UImageViewer


class UCentralWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.gridLayout = QGridLayout(self)

        self.uDestination = UDestination(self)
        self.gridLayout.addWidget(self.uDestination, 1, 0, 1, 1)

        self.uGenerate = UGenerate(self)

        self.gridLayout.addWidget(self.uGenerate, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self)
        self.uImageViewer = UImageViewer()
        self.tabWidget.addTab(self.uImageViewer, "Image Preview")
        self.uWatermarksList = UWatermarksList()
        self.tabWidget.addTab(self.uWatermarksList, "Watermarks")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.uImagesList = UImagesList(self)

        self.gridLayout.addWidget(self.uImagesList, 0, 1, 3, 1)
