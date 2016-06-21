# coding:utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsGraduatedSymbolRendererV2Widget
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
graduated_symbol_renderer_v2_widget = QgsGraduatedSymbolRendererV2Widget(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

graduated_symbol_renderer_v2_widget.setMapCanvas(canvas)


def on_widget_changed():
    layer.setRendererV2(
        graduated_symbol_renderer_v2_widget.renderer()
    )
    if canvas.isCachingEnabled():
        layer.setCacheImage(None)
        layer.triggerRepaint()
    else:
        canvas.refresh()

graduated_symbol_renderer_v2_widget.widgetChanged.connect(on_widget_changed)
graduated_symbol_renderer_v2_widget.show()
