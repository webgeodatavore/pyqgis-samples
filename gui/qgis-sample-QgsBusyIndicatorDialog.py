# coding: utf-8
from PyQt4.QtCore import Qt
from qgis.gui import QgsBusyIndicatorDialog
from qgis.utils import iface

busy_indicator_dialog = QgsBusyIndicatorDialog("Waiting", iface.mainWindow(),
                                               fl=Qt.WindowFlags())

busy_indicator_dialog.show()
