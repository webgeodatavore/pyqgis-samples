# coding: utf-8
from qgis.gui import QgsCustomLayerOrderWidget
from qgis.utils import iface

layer_tree_canvas_bridge = iface.layerTreeCanvasBridge()
custom_layer_order_widget = QgsCustomLayerOrderWidget(
    layer_tree_canvas_bridge
)

custom_layer_order_widget.show()
