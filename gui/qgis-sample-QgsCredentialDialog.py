# coding: utf-8
from PyQt4.QtCore import Qt  # http://doc.qt.io/qt-4.8/qwidget.html#windowFlags-prop
from qgis.gui import QgsCredentialDialog
from qgis.utils import iface

main_window = iface.mainWindow()
credential_dialog = QgsCredentialDialog(
    main_window,
    fl=Qt.WindowFlags()
)

credential_dialog.setModal(True)

credential_dialog.show()
