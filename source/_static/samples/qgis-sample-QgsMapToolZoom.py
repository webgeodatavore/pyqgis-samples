# coding: utf-8
from qgis.gui import QgsMapToolZoom
from qgis.utils import iface

canvas = iface.mapCanvas()
map_tool_zoom_in = QgsMapToolZoom(canvas, False)  # To zoom in
map_tool_zoom_out = QgsMapToolZoom(canvas, True)  # To zoom out

# Change tool to zoom in
canvas.setMapTool(map_tool_zoom_in)

# Change tool again to zoom out
canvas.setMapTool(map_tool_zoom_out)

# Reuse the existing QgsMapToolZoom zoomout instead of creating another one
iface.actionZoomOut().trigger()
# Reuse the existing QgsMapToolZoom zoomin instead of creating another one
iface.actionZoomIn().trigger()
