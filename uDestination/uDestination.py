__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class UDestination(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.gridLayout = QGridLayout(self)
        self.lineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self)
        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.label = QLabel(self)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        self.pushButton = QPushButton(self)

        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)

        self.radioButton = QRadioButton(self)

        self.gridLayout.addWidget(self.radioButton, 0, 1, 1, 3)
