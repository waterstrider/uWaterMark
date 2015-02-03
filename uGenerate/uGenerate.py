__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class UGenerate(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.generateButton = QPushButton(self)

        self.gridLayout.addWidget(self.generateButton, 0, 0, 2, 1)

        self.comboBox = QComboBox(self)

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.browseButton = QPushButton(self, "...")

        self.gridLayout.addWidget(self.browseButton, 1, 2, 1, 1)

        self.generateLabel = QLabel("Generate!", self)

        self.gridLayout.addWidget(self.generateLabel, 0, 1, 1, 2)
