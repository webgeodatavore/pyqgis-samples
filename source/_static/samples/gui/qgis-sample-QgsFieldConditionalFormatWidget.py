# coding: utf-8
from qgis.gui import QgsFieldConditionalFormatWidget
from qgis.utils import iface

layer = iface.activeLayer()
field_conditional_format_widget = QgsFieldConditionalFormatWidget()
field_conditional_format_widget.setLayer(layer)

field_conditional_format_widget.show()
