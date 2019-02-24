# coding: utf-8
from PyQt4.QtCore import Qt  # http://doc.qt.io/qt-4.8/qwidget.html#windowFlags-prop
from qgis.gui import QgsDashSpaceDialog
from qgis.utils import iface

main_window = iface.mainWindow()
dash_dialog = QgsDashSpaceDialog(
    [3.1, 1.1, 4.9, 6, 8],
    main_window,
    f=Qt.WindowFlags()
)

dash_dialog.show()
