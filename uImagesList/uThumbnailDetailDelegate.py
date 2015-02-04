__author__ = 'Shiraga-P'

from sys import argv

from PySide.QtCore import *
from PySide.QtGui import *

class UThumbnailDetailDelegate(QItemDelegate):
    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)

    def paint(self, painter, option, index):
        index.data(Qt.DisplayRole).render(painter, painter.deviceTransform().map(option.rect.topLeft()))