# coding: utf-8
from qgis.gui import QgsAttributeTypeLoadDialog
from qgis.utils import iface

layer = iface.activeLayer()
attribute_type_load_dialog = QgsAttributeTypeLoadDialog(layer)

attribute_type_load_dialog.show()
