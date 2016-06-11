# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsInvertedPolygonRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()

inverted_polygon_renderer_widget = QgsInvertedPolygonRendererWidget(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

inverted_polygon_renderer_widget.show()
