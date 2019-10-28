# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsSymbolV2SelectorDialog
from qgis.utils import iface

layer = iface.activeLayer()
symbol_v2_selector_dialog = QgsSymbolV2SelectorDialog(
    layer.rendererV2().symbol(),  # Symbol,
    QgsStyleV2.defaultStyle(),  # Style,
    layer,  # QgsVectorLayer
    None,  # Parent
    False  # Embedded
)

symbol_v2_selector_dialog.show()
