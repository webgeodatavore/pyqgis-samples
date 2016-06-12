# coding: utf-8
from qgis.gui import QgsPointPatternFillSymbolLayerWidget
from qgis.utils import iface

layer = iface.activeLayer()
point_pattern_fill_symbol_layer_widget = QgsPointPatternFillSymbolLayerWidget(
    layer
)

point_pattern_fill_symbol_layer_widget.show()
