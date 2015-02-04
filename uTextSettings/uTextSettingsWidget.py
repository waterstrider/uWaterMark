__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UTextSettingsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.textFormatWidget = QWidget(self)
        self.textFormatGridLayout = QGridLayout(self.textFormatWidget)

        self.boldButton = QPushButton("B", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.boldButton, 0, 1, 1, 1)

        self.fontButton = QPushButton("Font...", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.fontButton, 0, 0, 1, 1)

        self.leftButton = QPushButton("|<-", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.leftButton, 0, 3, 1, 1)

        self.italicButton = QPushButton("I", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.italicButton, 0, 2, 1, 1)

        self.centreButton = QPushButton("->|<-", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.centreButton, 0, 4, 1, 1)

        self.rightButton = QPushButton("->", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.rightButton, 0, 5, 1, 1)

        self.opacityLabel = QLabel("Opacity:", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.opacityLabel, 0, 6, 1, 1)

        self.colorPreviewLabel = QLabel(self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.colorPreviewLabel, 0, 9, 1, 1)

        self.colorLabel = QLabel("Color:", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.colorLabel, 0, 8, 1, 1)

        self.opacitySlider = QSlider(self.textFormatWidget)
        self.opacitySlider.setOrientation(Qt.Horizontal)

        self.textFormatGridLayout.addWidget(self.opacitySlider, 0, 7, 1, 1)

        self.colorButton = QPushButton("...", self.textFormatWidget)

        self.textFormatGridLayout.addWidget(self.colorButton, 0, 10, 1, 1)

        self.gridLayout.addWidget(self.textFormatWidget, 0, 0, 1, 1)

        self.textWidget = QWidget(self)
        self.textGridLayout = QGridLayout(self.textWidget)
        self.copyrightButton = QPushButton("©", self.textWidget)

        self.textGridLayout.addWidget(self.copyrightButton, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.textWidget)

        self.textGridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.textWidget)

        self.textGridLayout.addWidget(self.plainTextEdit, 0, 0, 2, 1)

        self.infoCombo = QComboBox(self.textWidget)

        self.textGridLayout.addWidget(self.infoCombo, 0, 1, 1, 2)

        self.gridLayout.addWidget(self.textWidget, 1, 0, 1, 1)
