__author__ = 'waterstrider.vin'

from PySide.QtGui import *

from uWatermarksList.uWatermarksListWidget import UWatermarksListWidget
from uImagesList.uImagesListWidget import UImagesListWidget
from uGenerate.uGenerateWidget import UGenerateWidget
from uDestination.uDestinationWidget import UDestinationWidget
from uImagePreview.uImagePreviewWidget import UImagePreviewWidget


class UCentralWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)

        self.uDestination = UDestinationWidget(self)
        self.gridLayout.addWidget(self.uDestination, 1, 0, 1, 1)

        self.uGenerate = UGenerateWidget(self)

        self.gridLayout.addWidget(self.uGenerate, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self)
        self.uImageViewer = UImagePreviewWidget()
        self.tabWidget.addTab(self.uImageViewer, "Image Preview")
        self.uWatermarksList = UWatermarksListWidget()
        self.tabWidget.addTab(self.uWatermarksList, "Watermarks")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.uImagesList = UImagesListWidget(self)

        self.gridLayout.addWidget(self.uImagesList, 0, 1, 3, 1)
