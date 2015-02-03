__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from uPushButton.uPushButtonWidget import UPushButtonWidget


class UImageViewerWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.gridLayout = QGridLayout(self)
        self.showAllWatermarksBox = QCheckBox("Show all watermarks", self)

        self.gridLayout.addWidget(self.showAllWatermarksBox, 1, 2, 1, 1)

        self.actualSizeButton = UPushButtonWidget(self, "Actual Size", "1:1")

        self.gridLayout.addWidget(self.actualSizeButton, 1, 1, 1, 1)

        self.fitToWindowButton = UPushButtonWidget(self, "Fit to Window", "<>")

        self.gridLayout.addWidget(self.fitToWindowButton, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.imageLabel = QLabel()

        self.scrollArea.setWidget(self.imageLabel)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)