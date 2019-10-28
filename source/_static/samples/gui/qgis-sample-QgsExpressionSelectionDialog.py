# coding: utf-8
from qgis.gui import QgsExpressionSelectionDialog
from qgis.utils import iface

layer = iface.activeLayer()
expression_selection_dialog = QgsExpressionSelectionDialog(layer, '"whatever"')

expression_selection_dialog.show()
