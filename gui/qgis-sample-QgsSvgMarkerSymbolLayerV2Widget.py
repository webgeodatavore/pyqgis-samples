# coding: utf-8
from qgis.gui import QgsSvgMarkerSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
svg_marker_symbol_layer_v2_widget = QgsSvgMarkerSymbolLayerV2Widget(layer)
svg_marker_symbol_layer_v2_widget.show()
