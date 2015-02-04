__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt

class UPresetsListWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.frame = QFrame(self)

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frameGridLayout = QGridLayout(self.frame)

        self.widget = QWidget(self.frame)

        self.presetsListGridLayout = QGridLayout(self.widget)

        self.addButton = QPushButton("+", self.widget)

        self.presetsListGridLayout.addWidget(self.addButton, 1, 1, 1, 1)

        self.applyButton = QPushButton("Apply", self.widget)

        self.presetsListGridLayout.addWidget(self.applyButton, 1, 0, 1, 1)

        self.removeButton = QPushButton("-", self.widget)

        self.presetsListGridLayout.addWidget(self.removeButton, 1, 2, 1, 1)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setWidgetResizable(True)
        self.uPresetsList = QListWidget()
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidget(self.uPresetsList)

        self.presetsListGridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)

        self.frameGridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

