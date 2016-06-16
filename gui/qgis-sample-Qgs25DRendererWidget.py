# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import Qgs25DRendererWidget
from qgis.utils import iface

renderer_25D_widget = Qgs25DRendererWidget(
    iface.activeLayer(),
    QgsStyleV2.defaultStyle(),
    iface.activeLayer().rendererV2()
)

renderer_25D_widget.show()

renderer_25D_widget_create = Qgs25DRendererWidget.create(
    iface.activeLayer(),
    QgsStyleV2.defaultStyle(),
    iface.activeLayer().rendererV2()
)

renderer_25D_widget_create.show()
