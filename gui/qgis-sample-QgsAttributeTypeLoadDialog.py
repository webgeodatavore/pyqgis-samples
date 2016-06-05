# coding: utf-8
from qgis.gui import QgsAttributeTypeLoadDialog
from qgis.utils import iface

attribute_type_load_dialog = QgsAttributeTypeLoadDialog(iface.activeLayer())

attribute_type_load_dialog.show()
