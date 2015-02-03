__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class UTextWatermarkWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.gridLayout = QGridLayout(self)