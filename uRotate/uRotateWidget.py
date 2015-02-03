__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class URotateWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.rotateGridLayout = QGridLayout(self)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frameGridLayout = QGridLayout(self.frame)

        self.angleWidget = QWidget(self.frame)

        self.angleGridLayout = QGridLayout(self.angleWidget)

        self.angle0Button = QPushButton("0°", self.angleWidget)

        self.angleGridLayout.addWidget(self.angle0Button, 0, 1, 1, 1)

        self.angle90Button = QPushButton("90°", self.angleWidget)

        self.angleGridLayout.addWidget(self.angle90Button, 1, 1, 1, 1)

        self.angle180Button = QPushButton("180°", self.angleWidget)

        self.angleGridLayout.addWidget(self.angle180Button, 2, 1, 1, 1)

        self.angle270Button = QPushButton("270°", self.angleWidget)

        self.angleGridLayout.addWidget(self.angle270Button, 3, 1, 1, 1)

        self.angleDialWidget = QWidget(self.angleWidget)

        self.angleDialGridLayout = QGridLayout(self.angleDialWidget)

        self.angleLabel = QLabel("Angle:", self.angleDialWidget)

        self.angleDialGridLayout.addWidget(self.angleLabel, 1, 0, 1, 1)

        self.angleSpin = QSpinBox(self.angleDialWidget)

        self.angleDialGridLayout.addWidget(self.angleSpin, 1, 1, 1, 1)

        self.angleDial = QDial(self.angleDialWidget)

        self.angleDialGridLayout.addWidget(self.angleDial, 0, 0, 1, 2)

        self.angleGridLayout.addWidget(self.angleDialWidget, 0, 0, 4, 1)

        self.frameGridLayout.addWidget(self.angleWidget, 0, 0, 1, 1)

        self.rotateGridLayout.addWidget(self.frame, 0, 0, 1, 1)