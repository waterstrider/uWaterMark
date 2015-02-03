__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UPositionWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.gridLayout = QGridLayout(self)
        self.frame = QFrame(self)

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)

        self.splitter = QSplitter(self.frame)

        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)

        self.gridLayout_2 = QGridLayout(self.widget)

        self.modeLabel = QLabel("Mode:", self.widget)

        self.gridLayout_2.addWidget(self.modeLabel, 0, 0, 1, 1)

        self.modeCombo = QComboBox(self.widget)

        self.gridLayout_2.addWidget(self.modeCombo, 0, 1, 1, 1)

        self.splitter.addWidget(self.widget)
        self.widget_2 = QWidget(self.splitter)

        self.gridLayout_3 = QGridLayout(self.widget_2)

        self.XOffsetSpin = QSpinBox(self.widget_2)

        self.gridLayout_3.addWidget(self.XOffsetSpin, 1, 1, 1, 1)

        self.XOffsetLabel = QLabel(self.widget_2)

        self.gridLayout_3.addWidget(self.XOffsetLabel, 0, 1, 1, 1)

        self.YOffsetLabel = QLabel(self.widget_2)

        self.gridLayout_3.addWidget(self.YOffsetLabel, 2, 1, 1, 1)

        self.YOffsetSpin = QSpinBox(self.widget_2)

        self.gridLayout_3.addWidget(self.YOffsetSpin, 3, 1, 1, 1)

        self.widget_3 = QWidget(self.widget_2)

        self.gridLayout_4 = QGridLayout(self.widget_3)

        self.pushButton_2 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_3)

        self.gridLayout_4.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 4, 1)

        self.splitter.addWidget(self.widget_2)

        self.gridLayout_5.addWidget(self.splitter, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
