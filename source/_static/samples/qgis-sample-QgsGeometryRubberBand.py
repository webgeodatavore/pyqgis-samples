# coding: utf-8
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QColor
from qgis.core import QGis, QgsPointV2, QgsLineStringV2, QgsPolygonV2
from qgis.gui import QgsGeometryRubberBand
from qgis.utils import iface

canvas = iface.mapCanvas()

# To show a point (Replace QgsVertexMarker if you are using QgsAbstractGeometryV2 geometries)
r_point = QgsGeometryRubberBand(canvas, QGis.Point)
point = QgsPointV2(2, 1)
r_point.setGeometry(point)

# To show a polyline (Replace QgsRubberBand if you are using QgsAbstractGeometryV2 geometries)
r_polyline = QgsGeometryRubberBand(canvas, QGis.Line)
points = [QgsPointV2(-1, -1), QgsPointV2(0, 1), QgsPointV2(1, -1)]
linestring_polyline = QgsLineStringV2()
linestring_polyline.setPoints(points)
r_polyline.setGeometry(linestring_polyline)

# To show a polygon (Replace QgsRubberBand if you are using QgsAbstractGeometryV2 geometries)
r_polygon = QgsGeometryRubberBand(canvas, QGis.Polygon)
points = [QgsPointV2(3, 5), QgsPointV2(5, 9), QgsPointV2(8, 5)]
linestring_polygon = QgsLineStringV2()
linestring_polygon.setPoints(points)
polygon = QgsPolygonV2()
polygon.setExteriorRing(linestring_polygon)
r_polygon.setGeometry(polygon)

# Customize rubber band
r_polygon.setBrushStyle(Qt.SolidPattern)
r_polygon.setFillColor(QColor('blue'))
r_polygon.setOutlineWidth(3)
r_polygon.setOutlineColor(QColor(255, 0, 255))
canvas.refresh()

# Remove the point, polyline and polygon QgsGeometryRubberBand band items
# canvas.scene().removeItem(r_point)
# canvas.scene().removeItem(r_polyline)
# canvas.scene().removeItem(r_polygon)
