# coding: utf-8
from qgis.core import QgsCoordinateReferenceSystem
from qgis.gui import QgsExtentGroupBox
from qgis.utils import iface

canvas = iface.mapCanvas()
canvas_extent = canvas.extent()
print(
    canvas_extent.xMinimum(),
    canvas_extent.xMaximum(),
    canvas_extent.yMinimum(),
    canvas_extent.yMaximum()
)

extent_group_box = QgsExtentGroupBox()
extent_group_box.setOriginalExtent(
    canvas_extent,
    canvas.mapSettings().destinationCrs()
)
extent_group_box.setCurrentExtent(
    canvas_extent,
    QgsCoordinateReferenceSystem('EPSG:3857')
)
extent_group_box.setOutputCrs(QgsCoordinateReferenceSystem('EPSG:3857'))

extent_group_box.show()
