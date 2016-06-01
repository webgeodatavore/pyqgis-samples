# coding: utf-8
from PyQt4.QtCore import Qt
from qgis.gui import QgsCharacterSelectorDialog

character_selector_dialog = QgsCharacterSelectorDialog(iface.mainWindow(), fl=Qt.WindowFlags())

character_selector_dialog.show()
