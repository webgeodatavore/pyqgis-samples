# coding: utf-8
from PyQt4.QtCore import Qt
from qgis.gui import QgsCharacterSelectorDialog
from qgis.utils import iface

main_window = iface.mainWindow()
character_selector_dialog = QgsCharacterSelectorDialog(
    main_window,
    fl=Qt.WindowFlags()
)

character_selector_dialog.show()
