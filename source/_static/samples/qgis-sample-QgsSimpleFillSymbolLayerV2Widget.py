# coding: utf-8
from qgis.gui import QgsSimpleFillSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()

simple_fill_symbol_layer_v2_widget = QgsSimpleFillSymbolLayerV2Widget(
    layer
)

simple_fill_symbol_layer_v2_widget.show()
