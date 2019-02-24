# coding: utf-8
from PyQt4.QtCore import QSizeF
from PyQt4.QtGui import QColor
from qgis.core import QgsPoint
from qgis.gui import QgsHtmlAnnotationItem
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
html_annotation_item = QgsHtmlAnnotationItem(
    canvas,
    layer
)
X, Y = float(3), float(45)
point = QgsPoint(X, Y)
html_annotation_item.setMapPosition(point)
html_annotation_item.setFrameSize(QSizeF(300, 200))
html_annotation_item.setFrameColor(QColor(0, 255, 0))
html_annotation_item.setFrameBackgroundColor(QColor(128, 128, 128))

html_content = """<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>
<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames
 ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget,
 tempor sit amet, ante. Donec eu libero sit amet quam egestas semper.
 Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet
 est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed,
 commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt
 condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec
 non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id
 cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat.
 Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor,
 facilisis luctus, metus
</p>
</body>
</html>
"""
html_url = "/tmp/index.html"  # Change the path on Windows

with open(html_url, 'wb') as f:
    f.write(html_content)

html_annotation_item.setHTMLPage(html_url)
canvas.refresh()

# You can remove the component with:
# iface.mapCanvas().scene().removeItem(html_annotation_item)
