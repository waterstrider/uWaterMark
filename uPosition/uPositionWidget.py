__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UPositionWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.positionGridLayout = QGridLayout(self)
        self.frame = QFrame(self)

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frameGridLayout = QGridLayout(self.frame)

        self.splitter = QSplitter(self.frame)

        self.splitter.setOrientation(Qt.Vertical)
        self.modeWidget = QWidget(self.splitter)

        self.modeGridLayout = QGridLayout(self.modeWidget)

        self.modeLabel = QLabel("Mode:", self.modeWidget)

        self.modeGridLayout.addWidget(self.modeLabel, 0, 0, 1, 1)

        self.modeCombo = QComboBox(self.modeWidget)

        self.modeGridLayout.addWidget(self.modeCombo, 0, 1, 1, 1)

        self.splitter.addWidget(self.modeWidget)
        self.borderOffsetWidget = QWidget(self.splitter)

        self.borderOffsetGridLayout = QGridLayout(self.borderOffsetWidget)

        self.XOffsetSpin = QSpinBox(self.borderOffsetWidget)

        self.borderOffsetGridLayout.addWidget(self.XOffsetSpin, 1, 1, 1, 1)

        self.XOffsetLabel = QLabel("X-Offset:", self.borderOffsetWidget)

        self.borderOffsetGridLayout.addWidget(self.XOffsetLabel, 0, 1, 1, 1)

        self.YOffsetLabel = QLabel("Y-Offset:", self.borderOffsetWidget)

        self.borderOffsetGridLayout.addWidget(self.YOffsetLabel, 2, 1, 1, 1)

        self.YOffsetSpin = QSpinBox(self.borderOffsetWidget)

        self.borderOffsetGridLayout.addWidget(self.YOffsetSpin, 3, 1, 1, 1)

        self.borderWidget = QWidget(self.borderOffsetWidget)

        self.borderGridLayout = QGridLayout(self.borderWidget)

        self.topButton = QPushButton("-", self.borderWidget)

        self.borderGridLayout.addWidget(self.topButton, 0, 1, 1, 1)

        self.topRightButton = QPushButton("-|", self.borderWidget)

        self.borderGridLayout.addWidget(self.topRightButton, 0, 2, 1, 1)

        self.leftButton = QPushButton("|", self.borderWidget)

        self.borderGridLayout.addWidget(self.leftButton, 1, 2, 1, 1)

        self.rightButton = QPushButton("|", self.borderWidget)

        self.borderGridLayout.addWidget(self.rightButton, 1, 0, 1, 1)

        self.centreButton = QPushButton("O", self.borderWidget)

        self.borderGridLayout.addWidget(self.centreButton, 1, 1, 1, 1)

        self.topLeftButton = QPushButton("|-", self.borderWidget)

        self.borderGridLayout.addWidget(self.topLeftButton, 0, 0, 1, 1)

        self.bottomLeftButton = QPushButton("|_", self.borderWidget)

        self.borderGridLayout.addWidget(self.bottomLeftButton, 2, 0, 1, 1)

        self.bottomButton = QPushButton("_", self.borderWidget)

        self.borderGridLayout.addWidget(self.bottomButton, 2, 1, 1, 1)

        self.bottomRightButton = QPushButton("_|", self.borderWidget)

        self.borderGridLayout.addWidget(self.bottomRightButton, 2, 2, 1, 1)

        self.borderOffsetGridLayout.addWidget(self.borderWidget, 0, 0, 4, 1)

        self.splitter.addWidget(self.borderOffsetWidget)

        self.frameGridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.positionGridLayout.addWidget(self.frame, 0, 0, 1, 1)
