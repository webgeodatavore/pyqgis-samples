# coding: utf-8
import inspect
import os
from PyQt4.QtCore import QSizeF
from PyQt4.QtGui import QColor
from qgis.core import QgsPoint
from qgis.gui import QgsSvgAnnotationItem
from qgis.utils import iface

canvas = iface.mapCanvas()
svg_annotation_item = QgsSvgAnnotationItem(canvas)
X, Y = float(3), float(45)
point = QgsPoint(X, Y)
svg_annotation_item.setMapPosition(point)
svg_annotation_item.setFrameSize(QSizeF(300, 200))
svg_annotation_item.setFrameColor(QColor(0, 255, 0))
svg_annotation_item.setFrameBackgroundColor(QColor(128, 128, 128))

print(
    inspect.getfile(inspect.currentframe())
)  # script filename (usually with path)

svg_path = os.path.join(
    os.path.dirname(
        inspect.getfile(
            inspect.currentframe()
        )
    ),
    '../data/icons/qgis_icon.svg'
)

# Choose an alternate SVG file
svg_annotation_item.setFilePath(svg_path)
canvas.refresh()

# Remove from canevas
# canvas.scene().removeItem(svg_annotation_item)
