# coding: utf-8
from qgis.gui import QgsSimpleMarkerSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()

simple_marker_symbol_layer_v2_widget = QgsSimpleMarkerSymbolLayerV2Widget(
    layer
)

simple_marker_symbol_layer_v2_widget.show()
