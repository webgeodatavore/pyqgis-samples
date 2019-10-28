from qgis.gui import QgsAttributeDialog
from qgis.utils import iface

map_canvas = iface.mapCanvas()
layer = map_canvas.currentLayer()
feature = next(layer.getFeatures())
attribute_dialog = QgsAttributeDialog(layer, feature, True)
attribute_dialog.show()

attribute_dialog_from_iface = iface.getFeatureForm(layer, feature)
attribute_dialog_from_iface.show()
