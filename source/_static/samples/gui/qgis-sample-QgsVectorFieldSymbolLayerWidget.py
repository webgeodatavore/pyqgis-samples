# coding: utf-8
from qgis.gui import QgsVectorFieldSymbolLayerWidget
from qgis.utils import iface

layer = iface.activeLayer()
vector_field_symbol_layer_widget = QgsVectorFieldSymbolLayerWidget(
    layer
)

vector_field_symbol_layer_widget.show()
