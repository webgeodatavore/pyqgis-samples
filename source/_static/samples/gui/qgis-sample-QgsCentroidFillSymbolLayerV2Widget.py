# coding: utf-8
from qgis.gui import QgsCentroidFillSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
centroid_fill_symbol_layer_v2_widget = QgsCentroidFillSymbolLayerV2Widget(
    layer
)

centroid_fill_symbol_layer_v2_widget.show()
