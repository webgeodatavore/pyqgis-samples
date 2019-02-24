# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import Qgs25DRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()
renderer_25D_widget = Qgs25DRendererWidget(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

renderer_25D_widget.show()

renderer_25D_widget_create = Qgs25DRendererWidget.create(
    layer,
    QgsStyleV2.defaultStyle(),
    layer.rendererV2()
)

renderer_25D_widget_create.show()
