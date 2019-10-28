# coding: utf-8
from qgis.gui import QgsExpressionBuilderDialog
from qgis.utils import iface

layer = iface.activeLayer()
expression_builder_dialog = QgsExpressionBuilderDialog(layer, '"whatever"')

expression_builder_dialog.show()
