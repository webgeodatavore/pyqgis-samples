# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsStyleV2GroupSelectionDialog

style_v2_group_selection_dialog = QgsStyleV2GroupSelectionDialog(
    QgsStyleV2.defaultStyle()
)

style_v2_group_selection_dialog.show()
