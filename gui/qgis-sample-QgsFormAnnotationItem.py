# coding: utf-8
from inspect import getsourcefile
import os
from PyQt4.QtCore import QPointF, QSizeF
from qgis.core import QgsPoint
from qgis.gui import QgsFormAnnotationItem
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
directory = os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))
form_annotation_item = QgsFormAnnotationItem(canvas, layer)
form_annotation_item.setMapPosition(QgsPoint(20, 40))
form_annotation_item.setDesignerForm(os.path.join(directory, '../ui/QgsFormAnnotationItemDemoFile.ui'))
form_annotation_item.setFrameSize(QSizeF(136.0, 50.0))
form_annotation_item.setOffsetFromReferencePoint(QPointF(-68.0, -75.0))
