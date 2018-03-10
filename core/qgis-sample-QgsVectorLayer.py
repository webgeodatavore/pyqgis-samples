# coding: utf-8
import urlparse
from qgis.core import QgsVectorLayer
from qgis.utils import iface

layer = iface.activeLayer()
if layer.providerType() == 'virtual':
    url_params = layer.source()[1:]  # To remove the ? at the beginning
    params_dict = urlparse.parse_qsl(url_params)
    params = dict(params_dict)
    print(params)
    print(params['query'])

SELECT "resultats-definitifs-consultation-26-juin-2016".*,
"communes44".*, ST_PointOnSurface("communes44".geometry) as geom
FROM "communes44", "resultats-definitifs-consultation-26-juin-2016"
WHERE "communes44"."INSEE_COM" = "resultats-definitifs-consultation-26-juin-2016"."code_insee"

CASE
WHEN ("oui_p" > 50 AND "oui_p" <= 57.7) THEN  color_rgb(247, 251, 255)
WHEN ("oui_p" > 57.7 AND "oui_p" <= 63.6) THEN  color_rgb(114, 178, 215)
WHEN ("oui_p" > 63.6 AND "oui_p" <= 85.1) THEN  color_rgb(8, 48, 107)
WHEN ("non_p" > 50 AND "non_p" <= 51.8) THEN  color_rgb(254, 240, 217)
WHEN ("non_p" > 51.8 AND "non_p" <= 57.1) THEN  color_rgb(252, 141, 89)
WHEN ("non_p" > 57.1 AND "non_p" <= 73.6) THEN  color_rgb(179, 0, 0)
END

from qgis.gui import QgsTextAnnotationItem;iface.mapCanvas().findChildren(QgsTextAnnotationItem)