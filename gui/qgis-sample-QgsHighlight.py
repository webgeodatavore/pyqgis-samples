# coding: utf-8
from PyQt4.QtCore import QVariant
from PyQt4.QtGui import QColor
from qgis.core import (QgsFeature, QgsField,
                       QgsGeometry, QgsPoint,
                       QgsMapLayerRegistry,
                       QgsVectorLayer)
from qgis.gui import QgsHighlight
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

highlight = QgsHighlight(
    iface.mapCanvas(),
    QgsGeometry.fromPoint(QgsPoint(0, 47)),
    vl
)
highlight.setBuffer(1.5)
highlight.setColor(QColor('black'))
highlight.setFillColor(QColor('blue'))
highlight.setWidth(0.5)
iface.mapCanvas().refresh()
