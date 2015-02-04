__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class USourceImageWidget(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.setTitle("Source Image")
        self.sourceImageGridLayout = QGridLayout(self)
        self.lineEdit = QLineEdit(self)

        self.sourceImageGridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.selectButton = QPushButton("Select", self)

        self.sourceImageGridLayout.addWidget(self.selectButton, 0, 1, 1, 1)

        self.embossBox = QCheckBox("Emboss image", self)

        self.sourceImageGridLayout.addWidget(self.embossBox, 1, 0, 1, 2)
