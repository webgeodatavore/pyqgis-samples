# coding: utf-8
from qgis.utils import iface
from qgis.gui import QgsAttributeDialog

map_canvas = iface.mapCanvas()
layer = map_canvas.currentLayer()
feature = layer.getFeatures().next()
dialog = QgsAttributeDialog(layer, feature, True)
dialog.show()
