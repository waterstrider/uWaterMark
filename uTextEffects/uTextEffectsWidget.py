__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import Qt


class UTextEffectsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.enableCheckBox = QCheckBox("Enable Effects", self)

        self.gridLayout.addWidget(self.enableCheckBox, 0, 0, 1, 2)

        self.embossGroupBox = QGroupBox("Emboss", self)
        self.embossGroupBox.setCheckable(True)
        self.embossGroupBox.setChecked(False)
        self.embossGridLayout = QGridLayout(self.embossGroupBox)
        self.upRadioButton = QRadioButton("Up", self.embossGroupBox)

        self.embossGridLayout.addWidget(self.upRadioButton, 0, 0, 1, 1)

        self.downRadioButton = QRadioButton("Down", self.embossGroupBox)

        self.embossGridLayout.addWidget(self.downRadioButton, 1, 0, 1, 1)

        self.embossButtonGroup = QButtonGroup(self)
        self.embossButtonGroup.addButton(self.upRadioButton)
        self.embossButtonGroup.addButton(self.downRadioButton)

        self.gridLayout.addWidget(self.embossGroupBox, 2, 1, 1, 1)

        self.shadowGroupBox = QGroupBox("Shadow", self)
        self.shadowGroupBox.setCheckable(True)
        self.shadowGroupBox.setChecked(False)
        self.shadowGridLayout = QGridLayout(self.shadowGroupBox)
        self.label_5 = QLabel(self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.label_5, 2, 4, 1, 1)

        self.colorButton = QPushButton("...", self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.colorButton, 2, 5, 1, 1)

        self.angleLabel = QLabel("Angle:", self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.angleLabel, 2, 1, 1, 1)

        self.opacityLabel = QLabel("Opacity:", self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.opacityLabel, 0, 1, 1, 1)

        self.distanceLabel = QLabel("Distance:", self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.distanceLabel, 1, 1, 1, 1)

        self.opacitySlider = QSlider(self.shadowGroupBox)
        self.opacitySlider.setOrientation(Qt.Horizontal)

        self.shadowGridLayout.addWidget(self.opacitySlider, 0, 2, 1, 4)

        self.dial = QDial(self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.dial, 0, 0, 3, 1)

        self.distanceSlider = QSlider(self.shadowGroupBox)
        self.distanceSlider.setOrientation(Qt.Horizontal)

        self.shadowGridLayout.addWidget(self.distanceSlider, 1, 2, 1, 4)

        self.angleSpinBox = QSpinBox(self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.angleSpinBox, 2, 2, 1, 1)

        self.colorLabel = QLabel("Color:", self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.colorLabel, 2, 3, 1, 1)

        self.opacitySpinBox = QSpinBox(self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.opacitySpinBox, 0, 6, 1, 1)

        self.distanceSpinBox = QSpinBox(self.shadowGroupBox)

        self.shadowGridLayout.addWidget(self.distanceSpinBox, 1, 6, 1, 1)

        self.gridLayout.addWidget(self.shadowGroupBox, 2, 0, 1, 1)
