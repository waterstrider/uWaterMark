__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UBackgroundWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.widget = QWidget(self)

        self.gridLayout_2 = QGridLayout(self.widget)

        self.label_2 = QLabel(self.widget)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSlider = QSlider(self.widget)

        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 1, 1, 2)

        self.label_3 = QLabel(self.widget)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.widget)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.widget)

        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_2, 1, 1, 1, 2)

        self.label_4 = QLabel(self.widget)

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.widget)

        self.gridLayout_2.addWidget(self.pushButton, 2, 2, 1, 1)

        self.spinBox = QSpinBox(self.widget)

        self.gridLayout_2.addWidget(self.spinBox, 0, 3, 1, 1)

        self.spinBox_2 = QSpinBox(self.widget)

        self.gridLayout_2.addWidget(self.spinBox_2, 1, 3, 1, 1)

        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        self.checkBox = QCheckBox(self)

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 2)

        self.line = QFrame(self)

        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.groupBox = QGroupBox(self)

        self.gridLayout_3 = QGridLayout(self.groupBox)

        self.label_6 = QLabel(self.groupBox)

        self.gridLayout_3.addWidget(self.label_6, 3, 6, 1, 1)

        self.label_7 = QLabel(self.groupBox)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 5, 1, 3)

        self.lineEdit_3 = QLineEdit(self.groupBox)

        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 1, 1, 4)

        self.lineEdit_4 = QLineEdit(self.groupBox)

        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 3, 1, 3)

        self.lineEdit = QLineEdit(self.groupBox)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 3, 1, 3)

        self.label_5 = QLabel(self.groupBox)

        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)

        self.gridLayout_3.addWidget(self.label_8, 1, 8, 1, 1)

        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)