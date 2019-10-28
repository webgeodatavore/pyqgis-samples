# coding: utf-8
from qgis.gui import QgsFontMarkerSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
font_marker_symbol_layer_v2_widget = QgsFontMarkerSymbolLayerV2Widget(layer)

font_marker_symbol_layer_v2_widget.show()
