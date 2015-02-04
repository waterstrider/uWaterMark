__author__ = 'Shiraga-P'

from sys import argv

from PySide.QtCore import *
from PySide.QtGui import *

class UThumbnailDetailDelegate(QItemDelegate):
    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)

    def paint(self, painter, option, index):
        value = index.data(Qt.DisplayRole)
        value.render(painter, painter.deviceTransform().map(option.rect.topLeft()))
        print(painter.deviceTransform().map(option.rect.topLeft()))