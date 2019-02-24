# coding: utf-8
from qgis.gui import QgsMapUnitScaleDialog
from qgis.utils import iface

map_unit_scale_dialog = QgsMapUnitScaleDialog()

print(map_unit_scale_dialog.getMapUnitScale())  # You can also set it using setMapUnitScale
print(map_unit_scale_dialog.getMapUnitScale().minScale)
print(map_unit_scale_dialog.getMapUnitScale().maxScale)
print(map_unit_scale_dialog.getMapUnitScale().minSizeMMEnabled)
print(map_unit_scale_dialog.getMapUnitScale().minSizeMM)
print(map_unit_scale_dialog.getMapUnitScale().maxSizeMMEnabled)
print(map_unit_scale_dialog.getMapUnitScale().maxSizeMM)

# Show for the first time
map_unit_scale_dialog.show()

# Change to be able to get scale from canvas
map_unit_scale_dialog.setMapCanvas(iface.mapCanvas())
# Show again to see the difference if you already closed the dialog
map_unit_scale_dialog.show()
