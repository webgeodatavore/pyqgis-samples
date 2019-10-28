# coding: utf-8
from inspect import getsourcefile
import os
from PyQt4.QtCore import QPointF, QSizeF
from qgis.core import QgsPoint
from qgis.gui import QgsFormAnnotationItem
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
directory = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
form_annotation_item = QgsFormAnnotationItem(canvas, layer)
form_annotation_item.setMapPosition(QgsPoint(20, 40))
# Data matching the form comes from
# http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
# Crash on our QGIS version 2.14.3 on Lubuntu 14.04 64 bits. Work with master
form_annotation_item.setDesignerForm(
    os.path.join(
        directory,
        '../ui/QgsFormAnnotationItemDemoFile.ui'
    )
)
form_annotation_item.setFrameSize(QSizeF(136.0, 50.0))
form_annotation_item.setOffsetFromReferencePoint(QPointF(-68.0, -75.0))

# Then remove
# canvas.scene().removeItem(form_annotation_item)
