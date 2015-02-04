__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from UTextSettings.UTextSettingsWidget import UTextSettingsWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uTextSettingsWidget = UTextSettingsWidget()
    uTextSettingsWidget.show()
    app.exec_()