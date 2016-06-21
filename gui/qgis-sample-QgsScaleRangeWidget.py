# coding: utf-8
from qgis.gui import QgsScaleRangeWidget
from qgis.utils import iface

canvas = iface.mapCanvas()

scale_range_widget = QgsScaleRangeWidget()
scale_range_widget.setMapCanvas(canvas)

scale_range_widget.show()
