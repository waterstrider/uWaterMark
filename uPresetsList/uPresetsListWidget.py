__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UPresetsListWidget(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.setTitle("Presets")

        self.presetsListGridLayout = QGridLayout(self)

        self.addButton = QPushButton("+", self)

        self.presetsListGridLayout.addWidget(self.addButton, 1, 1, 1, 1)

        self.applyButton = QPushButton("Apply", self)

        self.presetsListGridLayout.addWidget(self.applyButton, 1, 0, 1, 1)

        self.removeButton = QPushButton("-", self)

        self.presetsListGridLayout.addWidget(self.removeButton, 1, 2, 1, 1)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.uPresetsList = QListWidget()
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidget(self.uPresetsList)

        self.presetsListGridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)

