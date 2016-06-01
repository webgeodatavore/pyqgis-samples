# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsRendererV2PropertiesDialog
from qgis.utils import iface

renderer_v2_properties = QgsRendererV2PropertiesDialog(
    iface.activeLayer(),
    QgsStyleV2.defaultStyle(),
    True
)

renderer_v2_properties.show()
