__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UOpacityWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.frame = QFrame(self)

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)

        self.widget = QWidget(self.frame)

        self.gridLayout_3 = QGridLayout(self.widget)

        self.horizontalSlider = QSlider(self.widget)

        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider, 0, 0, 1, 1)

        self.label = QLabel(
            "0.......................................................................................100", self.widget)

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
