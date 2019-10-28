# coding:utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsSingleSymbolRendererV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
single_symbol_renderer_v2_widget = QgsSingleSymbolRendererV2Widget(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

single_symbol_renderer_v2_widget.setMapCanvas(canvas)


def on_widget_changed():
    layer.setRendererV2(
        single_symbol_renderer_v2_widget.renderer()
    )
    if canvas.isCachingEnabled():
        layer.setCacheImage(None)
        layer.triggerRepaint()
    else:
        canvas.refresh()

single_symbol_renderer_v2_widget.widgetChanged.connect(on_widget_changed)
single_symbol_renderer_v2_widget.show()
