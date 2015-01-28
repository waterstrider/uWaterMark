__author__ = 'waterstrider.vin'

from PySide.QtGui import *

from uWatermarksList
from uImagesList
from uGenerate
from


class UCentralWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.gridLayout = QGridLayout(self)

        self.widget_3 = QWidget(self)
        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 1)

        self.widget_2 = QWidget(self)

        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self)
        self.tab_5 = QWidget()
        self.tabWidget.addTab(self.tab_5, "Image Preview")
        self.tab_6 = QWidget()
        self.tabWidget.addTab(self.tab_6, "Watermarks")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.widget = QWidget(self)

        self.gridLayout.addWidget(self.widget, 0, 1, 3, 1)
