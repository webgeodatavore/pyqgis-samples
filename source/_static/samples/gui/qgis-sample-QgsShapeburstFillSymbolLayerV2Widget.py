# coding: utf-8
from qgis.gui import QgsShapeburstFillSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()

shapeburst_fill_symbol_layer_v2_widget = QgsShapeburstFillSymbolLayerV2Widget(
    layer
)

shapeburst_fill_symbol_layer_v2_widget.show()
