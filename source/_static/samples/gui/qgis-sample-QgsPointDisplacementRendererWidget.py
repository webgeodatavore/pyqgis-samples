# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsPointDisplacementRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()
point_displacement_renderer_widget = QgsPointDisplacementRendererWidget(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

point_displacement_renderer_widget.show()
