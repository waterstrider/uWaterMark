__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UWatermarksList(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)

        self.uWatermarksList = QListWidget()
        self.scrollArea.setWidget(self.uWatermarksList)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)

        self.addButton = QPushButton(self)

        self.gridLayout.addWidget(self.addButton, 2, 0, 1, 1)

        self.removeButton = QPushButton(self)

        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)

        self.loadButton = QPushButton(self)

        self.gridLayout.addWidget(self.loadButton, 0, 0, 1, 1)

        self.saveButton = QPushButton(self)

        self.gridLayout.addWidget(self.saveButton, 0, 1, 1, 1)