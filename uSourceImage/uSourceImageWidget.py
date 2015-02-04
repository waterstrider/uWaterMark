__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class USourceImageWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frameGridLayout = QGridLayout(self.frame)
        self.frameWidget = QWidget(self.frame)
        self.sourceImageGridLayout = QGridLayout(self.frameWidget)
        self.lineEdit = QLineEdit(self.frameWidget)

        self.sourceImageGridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.selectButton = QPushButton("Select", self.frameWidget)

        self.sourceImageGridLayout.addWidget(self.selectButton, 0, 1, 1, 1)

        self.embossBox = QCheckBox("Emboss image", self.frameWidget)

        self.sourceImageGridLayout.addWidget(self.embossBox, 1, 0, 1, 2)

        self.frameGridLayout.addWidget(self.frameWidget, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)