# coding: utf-8
from qgis.gui import QgsGradientFillSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
gradient_fill_symbol_layer_v2_widget = QgsGradientFillSymbolLayerV2Widget(
    layer
)

gradient_fill_symbol_layer_v2_widget.show()
