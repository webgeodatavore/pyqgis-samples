# coding: utf-8
from qgis.gui import QgsMapToolPan
from qgis.utils import iface

map_tool_pan = QgsMapToolPan(iface.mapCanvas())

iface.mapCanvas().setMapTool(map_tool_pan)

# Reuse the existing QgsMapToolPan instead of creating another one
iface.actionPan().trigger()
