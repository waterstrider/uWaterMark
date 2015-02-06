__author__ = 'waterstrider.vin'

from PySide.QtGui import *

from uImageViewer.uImageViewerWidget import UImageViewerWidget
from uPosition.uPositionWidget import UPositionWidget
from uRotate.uRotateWidget import URotateWidget
from uPresetsList.uPresetsListWidget import UPresetsListWidget
from uTextSettings.uTextSettingsWidget import UTextSettingsWidget
from uTextEffects.uTextEffectsWidget import UTextEffectsWidget

class UTextWatermarkWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Text Watermark")
        self.textWatermarkGridLayout = QGridLayout(self)
        self.previewFontWidget = QWidget(self)

        self.previewFontGridLayout = QGridLayout(self.previewFontWidget)

        self.uImageViewerWidget = UImageViewerWidget(self.previewFontWidget)

        self.previewFontGridLayout.addWidget(self.uImageViewerWidget, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.previewFontWidget)

        self.uTextSettingsWidget = UTextSettingsWidget()

        self.tabWidget.addTab(self.uTextSettingsWidget, "Text settings")
        self.uTextEffectsWidget = UTextEffectsWidget()

        self.tabWidget.addTab(self.uTextEffectsWidget, "Text effects")
        self.tab_5 = QWidget()

        self.tabWidget.addTab(self.tab_5, "Background")

        self.previewFontGridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.textWatermarkGridLayout.addWidget(self.previewFontWidget, 0, 0, 1, 1)

        self.presetsConfigWidget = QWidget(self)

        self.presetsConfigGridLayout = QGridLayout(self.presetsConfigWidget)

        self.buttonBox = QDialogButtonBox(self.presetsConfigWidget)

        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.presetsConfigGridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.uPositionWidget = UPositionWidget(self.presetsConfigWidget)

        self.presetsConfigGridLayout.addWidget(self.uPositionWidget, 0, 0, 1, 2)

        self.uRotateWidget = URotateWidget(self.presetsConfigWidget)

        self.presetsConfigGridLayout.addWidget(self.uRotateWidget, 1, 0, 1, 2)

        self.uPresetsListWidget = UPresetsListWidget(self.presetsConfigWidget)

        self.presetsConfigGridLayout.addWidget(self.uPresetsListWidget, 2, 0, 1, 2)

        self.textWatermarkGridLayout.addWidget(self.presetsConfigWidget, 0, 1, 1, 1)
