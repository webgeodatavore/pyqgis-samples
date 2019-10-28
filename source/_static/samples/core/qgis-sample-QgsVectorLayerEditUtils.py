# coding: utf-8
from PyQt4.QtCore import QVariant
from qgis.core import (QgsFeature,
                       QgsField, QgsGeometry,
                       QgsMapLayerRegistry,
                       QgsPoint,
                       QgsVectorLayer,
                       QgsVectorLayerEditUtils)

from qgis.utils import iface

# create layer
vl = QgsVectorLayer("Point?crs=epsg:4326&index=yes",
                    "temporary_points", "memory")
pr = vl.dataProvider()

# add fields
pr.addAttributes([
    QgsField("name", QVariant.String),
    QgsField("age", QVariant.Int),
    QgsField("size", QVariant.Double)
])
vl.updateFields()  # tell the vector layer to fetch changes from the provider

infos = [
    [10, 10, "John", 24, 1.73],
    [40, -60, "Paul", 29, 1.86],
    [60, 5, "George", 34, 1.69],
    [0, 45, "Ringo", 73, 1.75]
]

# add features
for i in infos:
    fet = QgsFeature()
    fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(i[0], i[1])))
    fet.setAttributes(i[2:5])
    pr.addFeatures([fet])

# update layer's extent when new features have been added
# because change of extent in provider is not propagated to the layer
vl.updateExtents()

QgsMapLayerRegistry.instance().addMapLayer(vl)

feat = vl.getFeatures().next()
canvas = iface.mapCanvas()

vector_layer_edit_utils = QgsVectorLayerEditUtils(vl)
vl.startEditing()
vector_layer_edit_utils.translateFeature(
    feat.id(),
    -5,  # dx
    1.0  # dy
)
vl.commitChanges()

# If caching is enabled, a simple canvas refresh might not be sufficient
# to trigger a redraw and you must clear the cached image for the layer
if canvas.isCachingEnabled():
    vl.setCacheImage(None)
else:
    canvas.refresh()
