# coding: utf-8
import inspect
import os
from PyQt4.QtCore import QSizeF
from PyQt4.QtGui import QColor
from qgis.core import QgsPoint
from qgis.gui import QgsSvgAnnotationItem
from qgis.utils import iface

annotationSvgItem = QgsSvgAnnotationItem(iface.mapCanvas())
X, Y = float(3), float(45)
point = QgsPoint(X, Y)
annotationSvgItem.setMapPosition(point)
annotationSvgItem.setFrameSize(QSizeF(300, 200))
annotationSvgItem.setFrameColor(QColor(0, 255, 0))
annotationSvgItem.setFrameBackgroundColor(QColor(128, 128, 128))

print(inspect.getfile(inspect.currentframe()))  # script filename (usually with path)

svg_path = os.path.join(
    os.path.dirname(
        inspect.getfile(
            inspect.currentframe()
        )
    ),
    '../data/icons/qgis_icon.svg'
)

# Choose an alternate SVG file
annotationSvgItem.setFilePath(svg_path)
iface.mapCanvas().refresh()

# Remove from canevas
# iface.mapCanvas().scene().removeItem(annotationSvgItem)
