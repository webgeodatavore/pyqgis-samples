# coding: utf-8

from qgis.core import QgsSnappingUtils
from qgis.gui import QgsMapCanvasSnappingUtils
from qgis.utils import iface

canvas = iface.mapCanvas()

snapping_utils = QgsSnappingUtils()
print(snapping_utils.snapToMapMode())
# Change the mode through the GUI
print(snapping_utils.snapToMapMode())
# Retrieve information from the project
snapping_utils.readConfigFromProject()

# Alternate way to above code
snapping_utils = canvas.snappingUtils()  # TODO: cast QgsMapCanvasSnappingUtils
snapping_utils.defaultSettings()

# Find the mode in a readable way
print([
    i for i in ['SnapCurrentLayer', 'SnapAdvanced', 'SnapAllLayers']
    if snapping_utils.snapToMapMode() == getattr(QgsSnappingUtils, i)
][0])


print(snapping_utils.layers())
print(snapping_utils.defaultSettings())  # where values are type, tolerance and unit

map_canvas_snapping_utils = QgsMapCanvasSnappingUtils(canvas)

canvas.setSnappingUtils(map_canvas_snapping_utils)
