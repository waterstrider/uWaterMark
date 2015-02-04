__author__ = 'waterstrider.vin'

from PySide.QtGui import *

from uImageViewer.uImageViewerWidget import UImageViewerWidget
from uSourceImage.uSourceImageWidget import USourceImageWidget
from uPosition.uPositionWidget import UPositionWidget
from uRotate.uRotateWidget import URotateWidget
from uOpacity.uOpacityWidget import UOpacityWidget


class UImageWatermarkWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.setWindowTitle("Image Watermark")
        self.uSourceImageWidget = USourceImageWidget(self)

        self.gridLayout.addWidget(self.uSourceImageWidget, 0, 1, 1, 1)

        self.uPositionWidget = UPositionWidget(self)

        self.gridLayout.addWidget(self.uPositionWidget, 1, 1, 1, 1)

        self.uRotateWidget = URotateWidget(self)

        self.gridLayout.addWidget(self.uRotateWidget, 2, 1, 1, 1)

        self.uOpacityWidget = UOpacityWidget(self)

        self.gridLayout.addWidget(self.uOpacityWidget, 3, 1, 1, 1)

        self.uImageViewerWidget = UImageViewerWidget(self)

        self.gridLayout.addWidget(self.uImageViewerWidget, 0, 0, 5, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)