__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class UPushButton(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.gridLayout = QGridLayout(self)

        self.pushButton = QPushButton(self)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label = QLabel(self)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
