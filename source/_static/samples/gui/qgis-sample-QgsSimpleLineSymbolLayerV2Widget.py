# coding: utf-8
from qgis.gui import QgsSimpleLineSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()

simple_line_symbol_layer_v2_widget = QgsSimpleLineSymbolLayerV2Widget(
    layer
)

simple_line_symbol_layer_v2_widget.show()
