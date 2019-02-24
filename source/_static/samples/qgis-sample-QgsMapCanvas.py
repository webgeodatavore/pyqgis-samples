# coding: utf-8
# Minimalist sample. For further, look at the plugin DockableMirrorMap code
from PyQt4.QtGui import QDialog
from qgis.core import QgsMapLayerRegistry
from qgis.gui import QgsMapCanvas, QgsMapCanvasLayer
from qgis.utils import iface

new_dialog = QDialog()
new_dialog.resize(800, 600)

map_canvas = QgsMapCanvas(new_dialog)
map_canvas.setMinimumSize(800, 600)

layers = QgsMapLayerRegistry.instance().mapLayers()
map_canvas_layer_list = [QgsMapCanvasLayer(l) for l in layers.values()]
map_canvas.setLayerSet(map_canvas_layer_list)
map_canvas.setExtent(iface.mapCanvas().extent())

new_dialog.show()
