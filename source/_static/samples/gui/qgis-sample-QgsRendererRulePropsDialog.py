# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsRendererRulePropsDialog
from qgis.utils import iface

layer = iface.activeLayer()  # You need a QgsVectorLayer with Rule-based style
canvas = iface.mapCanvas()
root_rule = layer.rendererV2().rootRule()
renderer_rule_props_dialog = QgsRendererRulePropsDialog(
    root_rule.children()[1].children()[0],  # QgsRuleBasedRendererV2.Rule
    layer,  # QgsVectorLayer
    QgsStyleV2.defaultStyle(),  # QgsStyleV2
    None,  # parent QWidget, optional
    canvas  # QgsMapCanvas, optional
)

renderer_rule_props_dialog.show()
