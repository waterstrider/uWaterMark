__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uPresetsList.uPresetsListWidget import UPresetsListWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uPresetsListWidget = UPresetsListWidget()
    uPresetsListWidget.show()
    app.exec_()