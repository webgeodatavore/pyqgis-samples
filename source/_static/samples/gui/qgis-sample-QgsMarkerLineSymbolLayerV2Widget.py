# coding: utf-8
from qgis.gui import QgsMarkerLineSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
marker_line_symbol_layer_v2_widget = QgsMarkerLineSymbolLayerV2Widget(
    layer
)

marker_line_symbol_layer_v2_widget.show()
