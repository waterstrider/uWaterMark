__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class UDestinationWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.gridLayout = QGridLayout(self)
        self.destinationPath = QLineEdit(self)
        self.gridLayout.addWidget(self.destinationPath, 1, 2, 1, 1)

        self.toFolderButton = QRadioButton("To Folder", self)
        self.gridLayout.addWidget(self.toFolderButton, 1, 1, 1, 1)

        self.destinationLabel = QLabel("Destination:", self)
        self.gridLayout.addWidget(self.destinationLabel, 0, 0, 1, 1)

        self.browseButton = QPushButton("...", self)
        self.gridLayout.addWidget(self.browseButton, 1, 3, 1, 1)

        self.originalFolderButton = QRadioButton("To Original Folder(s)", self)
        self.gridLayout.addWidget(self.originalFolderButton, 0, 1, 1, 3)
