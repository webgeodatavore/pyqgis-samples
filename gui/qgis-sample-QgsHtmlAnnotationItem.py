# coding: utf-8
from PyQt4.QtCore import QSizeF
from PyQt4.QtGui import QColor
from qgis.core import QgsPoint
from qgis.gui import QgsHtmlAnnotationItem
from qgis.utils import iface

htmlAnnotationItem = QgsHtmlAnnotationItem(
    iface.mapCanvas(),
    iface.activeLayer()
)
X, Y = float(3), float(45)
point = QgsPoint(X, Y)
htmlAnnotationItem.setMapPosition(point)
htmlAnnotationItem.setFrameSize(QSizeF(300, 200))
htmlAnnotationItem.setFrameColor(QColor(0, 255, 0))
htmlAnnotationItem.setFrameBackgroundColor(QColor(128, 128, 128))
html_url = "/tmp/index.html"

htmlAnnotationItem.setHTMLPage(html_url)
iface.mapCanvas().refresh()

# You can remove the component with:
# iface.mapCanvas().scene().removeItem(htmlAnnotationItem)
