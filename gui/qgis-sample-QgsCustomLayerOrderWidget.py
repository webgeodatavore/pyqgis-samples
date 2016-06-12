# coding: utf-8
from qgis.gui import QgsCustomLayerOrderWidget
from qgis.utils import iface

custom_layer_order_widget = QgsCustomLayerOrderWidget(
    iface.layerTreeCanvasBridge()
)

custom_layer_order_widget.show()
