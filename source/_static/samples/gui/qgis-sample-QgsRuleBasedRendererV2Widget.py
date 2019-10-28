# coding:utf-8
from PyQt4.QtGui import QTreeView
from qgis.core import QgsStyleV2
from qgis.gui import QgsRuleBasedRendererV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
rule_based_renderer_v2_widget = QgsRuleBasedRendererV2Widget(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

rule_based_renderer_v2_widget.setMapCanvas(canvas)


def on_widget_changed():
    layer.setRendererV2(
        rule_based_renderer_v2_widget.renderer()
    )
    if canvas.isCachingEnabled():
        layer.setCacheImage(None)
        layer.triggerRepaint()
    else:
        canvas.refresh()

rule_based_renderer_v2_widget.widgetChanged.connect(on_widget_changed)
rule_based_renderer_v2_widget.show()

print(
    rule_based_renderer_v2_widget.findChildren(
        QTreeView,
        "viewRules"
    )[0].model()
)  # Issue: it returns a PyQt4.QtCore.QAbstractItemModel whereas it should
# return a QgsRuleBasedRendererV2Model according to code e.g
# https://qgis.org/api/qgsrulebasedrendererv2widget_8cpp_source.html#l00068
