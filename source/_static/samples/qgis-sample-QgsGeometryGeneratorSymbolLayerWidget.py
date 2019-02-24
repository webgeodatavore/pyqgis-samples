# coding: utf-8
from qgis.gui import QgsGeometryGeneratorSymbolLayerWidget
from qgis.utils import iface

layer = iface.activeLayer()
geometry_generator_symbol_layer_widget = QgsGeometryGeneratorSymbolLayerWidget(
    layer
)

geometry_generator_symbol_layer_widget.show()
