# coding: utf-8
from PyQt4.QtCore import QSizeF
from PyQt4.QtGui import QColor, QTextDocument
from qgis.core import QgsPoint
from qgis.gui import QgsTextAnnotationItem
from qgis.utils import iface

annotationItem = QgsTextAnnotationItem(iface.mapCanvas())
X, Y = float(3), float(45)
point = QgsPoint(X, Y)
annotationItem.setMapPosition(point)
annotationItem.setFrameSize(QSizeF(300, 200))
annotationItem.setFrameColor(QColor(0, 255, 0))
annotationItem.setFrameBackgroundColor(QColor(128, 128, 128))
text_document = QTextDocument()
html_content = "<b>New annotation</b>"
font_color, font_family, font_size = "#123456", "Times New Roman", 16
text_document.setHtml('<font style="color:' + font_color +
                      "; font-family:" + font_family + "; font-size: " +
                      str(font_size) + 'px">' + html_content + "</font>")
annotationItem.setDocument(text_document)
iface.mapCanvas().refresh()

# Then remove
# iface.mapCanvas().scene().removeItem(annotationItem)
