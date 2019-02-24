# coding: utf-8
from PyQt4.QtCore import QSizeF
from PyQt4.QtGui import QColor, QTextDocument
from qgis.core import QgsPoint
from qgis.gui import QgsTextAnnotationItem
from qgis.utils import iface

canvas = iface.mapCanvas()
text_annotation_item = QgsTextAnnotationItem(canvas)
X, Y = float(3), float(45)
point = QgsPoint(X, Y)
text_annotation_item.setMapPosition(point)
text_annotation_item.setFrameSize(QSizeF(300, 200))
text_annotation_item.setFrameColor(QColor(0, 255, 0))
text_annotation_item.setFrameBackgroundColor(QColor(128, 128, 128))
text_document = QTextDocument()
html_content = "<b>New annotation</b>"
font_color, font_family, font_size = "#123456", "Times New Roman", 16
text_document.setHtml('<font style="color:' + font_color +
                      "; font-family:" + font_family + "; font-size: " +
                      str(font_size) + 'px">' + html_content + "</font>")
text_annotation_item.setDocument(text_document)
canvas.refresh()

# Then remove
# canvas.scene().removeItem(text_annotation_item)
