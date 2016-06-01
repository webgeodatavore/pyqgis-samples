# coding: utf-8
from PyQt4.QtCore import Qt  # http://doc.qt.io/qt-4.8/qwidget.html#windowFlags-prop
from qgis.core import QgsError
from qgis.gui import QgsErrorDialog
from qgis.utils import iface

error_dialog = QgsErrorDialog(
    QgsError("My error message", "My GDAL tag"),
    "My title",
    iface.mainWindow(),
    fl=Qt.WindowFlags()
)

error_dialog.show(
    QgsError("My error message", "My GDAL tag"),
    "My title",
    iface.mainWindow(),
    fl=Qt.WindowFlags()
)
