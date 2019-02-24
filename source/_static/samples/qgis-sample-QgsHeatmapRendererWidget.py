# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsHeatmapRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()

heatmap_renderer_widget = QgsHeatmapRendererWidget(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

heatmap_renderer_widget.show()
