# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsSmartGroupEditorDialog
from qgis.utils import iface

layer = iface.activeLayer()
smart_group_editor_dialog = QgsSmartGroupEditorDialog(
    QgsStyleV2.defaultStyle()
)

smart_group_editor_dialog.show()
