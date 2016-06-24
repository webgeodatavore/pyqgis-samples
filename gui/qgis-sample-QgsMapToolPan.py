# coding: utf-8
from qgis.gui import QgsMapToolPan
from qgis.utils import iface

canvas = iface.mapCanvas()
map_tool_pan = QgsMapToolPan(canvas)

canvas.setMapTool(map_tool_pan)

# Reuse the existing QgsMapToolPan instead of creating another one
iface.actionPan().trigger()
