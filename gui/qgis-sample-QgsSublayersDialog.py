# coding: utf-8
from qgis.core import (QgsLayerTreeLayer, QgsMapLayerRegistry,
                       QgsProject, QgsVectorLayer)
from qgis.gui import QgsSublayersDialog

sublayers_dialog = QgsSublayersDialog(QgsSublayersDialog.Ogr, 'Title')  # Try with QgsSublayersDialog.Gdal or QgsSublayersDialog.Vsifile

root = QgsProject.instance().layerTreeRoot()

layers = []
for child in root.children():
    if isinstance(child, QgsLayerTreeLayer):
        layer = QgsMapLayerRegistry.instance().mapLayer(child.layerId())
        if isinstance(layer, QgsVectorLayer):
            print("- layer: " + child.layerName() + "  ID: " + child.layerId())
            layers.append(
                '%s|%s|%s|%s' % (layer.id(), layer.name(),
                                 layer.featureCount(), layer.geometryType())
            )

sublayers_dialog.populateLayerTable(layers, delim="|")

sublayers_dialog.show()

# Then type after some line selection, below code
sublayers_dialog.selectionNames()
# Seems buggy here because when 2nd always return 0  > Confirm if bug
sublayers_dialog.selectionIndexes()
