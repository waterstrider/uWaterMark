__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uTextSettings.uTextSettingsWidget import UTextSettingsWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uTextSettingsWidget = UTextSettingsWidget()
    uTextSettingsWidget.show()
    app.exec_()