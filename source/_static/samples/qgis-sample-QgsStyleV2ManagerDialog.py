# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsStyleV2ManagerDialog

style_v2_manager_dialog = QgsStyleV2ManagerDialog(
    QgsStyleV2.defaultStyle()
)

style_v2_manager_dialog.show()
