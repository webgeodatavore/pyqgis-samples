# coding: utf-8
from qgis.gui import QgsLinePatternFillSymbolLayerWidget
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()

line_pattern_fill_symbol_layer_widget = QgsLinePatternFillSymbolLayerWidget(
    layer
)
line_pattern_fill_symbol_layer_widget.setMapCanvas(canvas)

line_pattern_fill_symbol_layer_widget.show()
