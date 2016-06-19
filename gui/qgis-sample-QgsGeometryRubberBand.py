# coding: utf-8
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QColor
from qgis.core import QGis, QgsPointV2, QgsLineStringV2, QgsPolygonV2
from qgis.gui import QgsGeometryRubberBand
from qgis.utils import iface

canvas = iface.mapCanvas()

# To show a point (Replace QgsVertexMarker if you are using QgsAbstractGeometryV2 geometries)
r = QgsGeometryRubberBand(canvas, QGis.Point)
point = QgsPointV2(2, 1)
r.setGeometry(point)

# Remove the rubber band item
canvas.scene().removeItem(r)

# To show a polyline (Replace QgsRubberBand if you are using QgsAbstractGeometryV2 geometries)
r = QgsGeometryRubberBand(canvas, QGis.Line)
points = [QgsPointV2(-1, -1), QgsPointV2(0, 1), QgsPointV2(1, -1)]
linestring = QgsLineStringV2()
linestring.setPoints(points)
r.setGeometry(linestring)

# Remove the rubber band item
canvas.scene().removeItem(r)

# To show a polygon (Replace QgsRubberBand if you are using QgsAbstractGeometryV2 geometries)
r = QgsGeometryRubberBand(canvas, QGis.Polygon)
points = [QgsPointV2(-1, -1), QgsPointV2(0, 1), QgsPointV2(1, -1)]
linestring = QgsLineStringV2()
linestring.setPoints(points)
polygon = QgsPolygonV2()
polygon.setExteriorRing(linestring)
r.setGeometry(polygon)

# Customize rubber band
r.setBrushStyle(Qt.SolidPattern)
r.setFillColor(QColor('blue'))
r.setOutlineWidth(3)
r.setOutlineColor(QColor(255, 0, 255))
canvas.refresh()

# Remove the rubber band item
canvas.scene().removeItem(r)
