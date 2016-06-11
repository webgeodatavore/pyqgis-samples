# coding: utf-8
from qgis.gui import QgsEllipseSymbolLayerV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
ellipse_symbol_layer_v2_widget = QgsEllipseSymbolLayerV2Widget(layer)

ellipse_symbol_layer_v2_widget.show()
