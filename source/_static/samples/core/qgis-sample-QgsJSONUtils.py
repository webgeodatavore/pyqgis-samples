# coding: utf-8
import codecs
import os
from PyQt4.QtCore import QTextCodec, QVariant
from qgis.core import (QgsApplication, QgsFeature, QgsField, QgsFields,
                       QgsGeometry, QgsJSONUtils, QgsPoint)
from qgis.utils import iface

geojson_contributors = os.path.join(
    os.path.dirname(QgsApplication.developersMapFilePath()),
    'contributors.json'
)
geojson_contributors_string = codecs.open(
    geojson_contributors,
    encoding='utf-8'
).read()

layer = iface.activeLayer()

# Encodes a value to a JSON string representation, adding appropriate
# quotations and escaping where required.
print(QgsJSONUtils.encodeValue([{"name": "George", "age": 34, "size": 1.69}]))

fields = QgsFields()
fields_list = [
    QgsField("name", QVariant.String),
    QgsField("age", QVariant.Int),
    QgsField("size", QVariant.Double)
]

for f in fields_list:
    fields.append(f)

feature = QgsFeature(fields)
feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(60, 5)))
feature.setAttributes(["George", 34, 1.69])

# Exports all attributes from a QgsFeature as a JSON map type.
with codecs.open('feature.json', 'wb', encoding='utf-8') as f:
    json_text = QgsJSONUtils.exportAttributes(feature)
    f.write(json_text)

# Attempts to retrieve the fields from a GeoJSON string representing a
# collection of features.
fields = QgsJSONUtils.stringToFields(
    geojson_contributors_string,
    QTextCodec.codecForName('UTF-8')
)

for f in fields:
    print(f.name(), f.type())

# Attempts to parse a GeoJSON string to a collection of features.
features = QgsJSONUtils.stringToFeatureList(
    geojson_contributors_string,
    fields,
    QTextCodec.codecForName('UTF-8')
)
print(features)
