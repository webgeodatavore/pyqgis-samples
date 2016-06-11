# coding: utf-8
from qgis.gui import QgsLayerPropertiesWidget
from qgis.utils import iface

layer = iface.activeLayer()
layer_properties_widget = QgsLayerPropertiesWidget(
    layer.rendererV2().symbol().symbolLayers()[0],
    layer.rendererV2().symbol(),
    layer
)

layer_properties_widget.show()
