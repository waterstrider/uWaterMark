__author__ = 'Shiraga-P'

from sys import argv

from PySide.QtCore import *
from PySide.QtGui import *

class UThumbnailDetailModel(QAbstractListModel):
    def __init__(self, dataList=[], parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)
        self.listdata = dataList

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)

    def addItem(self, data):
        self.listdata.append(data)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return self.listdata[index.row()].thumbnailWidget
        else:
            return


