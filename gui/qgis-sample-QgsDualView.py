# coding: utf-8
from qgis.gui import QgsDualView
from qgis.utils import iface

dv = QgsDualView()
dv.init(iface.activeLayer(), iface.mapCanvas())  # The active layer is a vector layer
dv.setView(QgsDualView.AttributeEditor)  # It could be QgsDualView.AttributeTable instead
dv.show()
