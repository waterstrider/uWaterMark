__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class URotateWidget(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.setTitle("Rotation")
        self.angleGridLayout = QGridLayout(self)

        self.angle0Button = QPushButton("0°", self)

        self.angleGridLayout.addWidget(self.angle0Button, 0, 1, 1, 1)

        self.angle90Button = QPushButton("90°", self)

        self.angleGridLayout.addWidget(self.angle90Button, 1, 1, 1, 1)

        self.angle180Button = QPushButton("180°", self)

        self.angleGridLayout.addWidget(self.angle180Button, 2, 1, 1, 1)

        self.angle270Button = QPushButton("270°", self)

        self.angleGridLayout.addWidget(self.angle270Button, 3, 1, 1, 1)

        self.angleDialWidget = QWidget(self)

        self.angleDialGridLayout = QGridLayout(self.angleDialWidget)

        self.angleLabel = QLabel("Angle:", self.angleDialWidget)

        self.angleDialGridLayout.addWidget(self.angleLabel, 1, 0, 1, 1)

        self.angleSpin = QSpinBox(self.angleDialWidget)

        self.angleDialGridLayout.addWidget(self.angleSpin, 1, 1, 1, 1)

        self.angleDial = QDial(self.angleDialWidget)

        self.angleDialGridLayout.addWidget(self.angleDial, 0, 0, 1, 2)

        self.angleGridLayout.addWidget(self.angleDialWidget, 0, 0, 4, 1)