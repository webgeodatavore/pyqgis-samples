# coding: utf-8
from qgis.utils import iface
from qgis.gui import QgsNewMemoryLayerDialog

new_memory_layer_dialog = QgsNewMemoryLayerDialog(iface.mainWindow())
new_memory_layer_dialog.show()
