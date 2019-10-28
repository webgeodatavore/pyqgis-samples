# coding: utf-8
from PyQt4.QtGui import QColor
from qgis.utils import iface
from qgis.core import QgsPoint
from qgis.gui import QgsVertexMarker

canvas = iface.mapCanvas()
m = QgsVertexMarker(canvas)
m.setCenter(QgsPoint(0, 0))

m.setColor(QColor(0, 0, 255))
m.setIconSize(7)
m.setIconType(QgsVertexMarker.ICON_BOX)  # See the enum IconType from http://www.qgis.org/api/classQgsVertexMarker.html
m.setPenWidth(3)

m.hide()
m.show()

# Remove the element
# canvas.scene().removeItem(m)
