__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uTextEffects.uTextEffectsWidget import UTextEffectsWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uTextEffectsWidget = UTextEffectsWidget()
    uTextEffectsWidget.show()
    app.exec_()