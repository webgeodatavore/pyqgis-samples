# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsRendererV2PropertiesDialog
from qgis.utils import iface

layer = iface.activeLayer()

renderer_v2_properties = QgsRendererV2PropertiesDialog(
    layer,
    QgsStyleV2.defaultStyle(),
    True
)

renderer_v2_properties.show()
