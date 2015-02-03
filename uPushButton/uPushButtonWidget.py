__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class UPushButtonWidget(QWidget):
    def __init__(self, parent=None, label=None, image=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)

        self.pushButton = QPushButton(image, self)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label = QLabel(label, self)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
