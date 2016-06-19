# coding: utf-8
from qgis.gui import QgsDualView
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
dv = QgsDualView()
dv.init(layer, canvas)  # The active layer is a vector layer
dv.setView(QgsDualView.AttributeEditor)  # It could be QgsDualView.AttributeTable instead
dv.show()
