# coding: utf-8
from PyQt4.QtCore import Qt  # http://doc.qt.io/qt-4.8/qwidget.html#windowFlags-prop
from PyQt4.QtGui import QColor  # http://doc.qt.io/qt-4.8/qcolor.html
from qgis.gui import QgsColorDialogV2
from qgis.utils import iface

color_dialog_v2 = QgsColorDialogV2(
    iface.mainWindow(),
    fl=Qt.WindowFlags(),
    color=QColor(0, 255, 127, 127)
)


def on_qcolor_changed(qcolor):
    print(qcolor.name())

color_dialog_v2.currentColorChanged.connect(on_qcolor_changed)

# new_dialog.show()
color_dialog_v2.show()

# Change default value to True to False
color_dialog_v2.setAllowAlpha(False)
