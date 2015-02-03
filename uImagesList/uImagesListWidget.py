__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt

from uPushButton.uPushButtonWidget import UPushButtonWidget


class UImagesListWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.addButton = UPushButtonWidget(self, "add", "+")
        self.gridLayout.addWidget(self.addButton, 1, 0, 1, 1)

        self.removeButton = UPushButtonWidget(self, "remove", "-")

        self.gridLayout.addWidget(self.removeButton, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)

        self.uImageList = QListWidget()
        self.scrollArea.setWidget(self.uImageList)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)