# coding: utf-8
from PyQt4.QtGui import QColor
from qgis.core import QgsGeometry, QgsPoint
from qgis.gui import QgsRubberBand
from qgis.utils import iface

canvas = iface.mapCanvas()
# To show a polyline
r = QgsRubberBand(canvas, False)  # False = not a polygon
points = [QgsPoint(-1, -1), QgsPoint(0, 1), QgsPoint(1, -1)]
r.setToGeometry(QgsGeometry.fromPolyline(points), None)

# To show a polygon
r = QgsRubberBand(canvas, True)  # True = a polygon
points = [[QgsPoint(-1, -1), QgsPoint(0, 1), QgsPoint(1, -1)]]
r.setToGeometry(QgsGeometry.fromPolygon(points), None)

# Customize rubber band
r.setColor(QColor(0, 0, 255))
r.setWidth(3)

# Remove the rubber band item
canvas.scene().removeItem(r)

# TODO: report addPoint method
