__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UOpacityWidget(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.setTitle("Opacity")

        self.opacityGridLayout = QGridLayout(self)

        self.horizontalSlider = QSlider(self)

        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.opacityGridLayout.addWidget(self.horizontalSlider, 0, 0, 1, 1)

        self.label = QLabel(
            "0.......................................................................................100", self)

        self.opacityGridLayout.addWidget(self.label, 1, 0, 1, 1)
