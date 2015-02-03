__author__ = 'Shiraga-P'

from sys import argv

from PySide.QtCore import *
from PySide.QtGui import *

class UThumbnailDetailItem(QWidget):
    def __init__(self, filepath,  parent=None):
        QWidget.__init__(self, parent)

        try:
            filepath = str(filepath)
        except:
            return -1                                                   # TODO: add warning

        self.thumbnailPixmap = QPixmap(filepath)
        self.thumbnailLabel = QLabel("<Thumbnail>")
        self.thumbnailLabel.setStyleSheet("border: 1px solid grey")
        self.thumbnailLabel.setPixmap(self.thumbnailPixmap.scaled(150, 150, Qt.KeepAspectRatio))

        filename = filepath[max(filepath.rfind('\\'), filepath.rfind('/')) + 1:]
        width = self.thumbnailPixmap.width()
        height = self.thumbnailPixmap.height()
        depth = self.thumbnailPixmap.depth()
        detailsGridLayout = QGridLayout(None)
        detailsGridLayout.addWidget(QLabel("Filename: " + filename), 0, 0, 1, 1)
        detailsGridLayout.addWidget(QLabel("Width: " + str(width) + " px"), 1, 0, 1, 1)
        detailsGridLayout.addWidget(QLabel("Height: " + str(height) + " px"), 2, 0, 1, 1)
        detailsGridLayout.addWidget(QLabel("Bit Depth: " + str(depth)), 3, 0, 1, 1)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.thumbnailLabel, 0, 0, 1, 1)
        self.gridLayout.addLayout(detailsGridLayout, 0, 1, 1, 1)


if __name__ == "__main__":
    app = QApplication(argv)
    uThumbnailDetail = UThumbnailDetailItem("..\\Resources\\Sample Image\\sample01.jpg")
    uThumbnailDetail.show()
    app.exec_()

