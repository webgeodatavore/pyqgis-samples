# coding: utf-8
from PyQt4.QtCore import QVariant
from qgis.core import (QgsFeature, QgsField, QgsFields,
                       QgsGeometry, QgsPoint, QgsVectorFileWriter)
from qgis.utils import QGis, iface
# Export a vector layer from a QgsVectorLayer

layer = iface.activeLayer()
error = QgsVectorFileWriter.writeAsVectorFormat(layer, "my_shapes.shp",
                                                "CP1250", None,
                                                "ESRI Shapefile")

if error == QgsVectorFileWriter.NoError:
    print("success!")

error = QgsVectorFileWriter.writeAsVectorFormat(layer, "my_json.json",
                                                "utf-8", None, "GeoJSON")
if error == QgsVectorFileWriter.NoError:
    print("success again!")

# Export a vector layer directly from features
# define fields for feature attributes. A QgsFields object is needed
fields = QgsFields()
fields.append(QgsField("first", QVariant.Int))
fields.append(QgsField("second", QVariant.String))

# Create an instance of vector file writer, which will create the vector file.
# Arguments:
# 1. path to new file (will fail if exists already)
# 2. encoding of the attributes
# 3. field map
# 4. geometry type - from WKBTYPE enum
# 5. layer's spatial reference (instance of
#    QgsCoordinateReferenceSystem) - optional
# 6. driver name for the output file
writer = QgsVectorFileWriter("my_shapes.shp", "CP1250", fields,
                             QGis.WKBPoint, None, "ESRI Shapefile")

if writer.hasError() != QgsVectorFileWriter.NoError:
    print("Error when creating shapefile: ", writer.errorMessage())

# Add a feature
fet = QgsFeature()
fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(10, 10)))
fet.setAttributes([1, "text"])
writer.addFeature(fet)

# Delete the writer to flush features to disk
del writer
