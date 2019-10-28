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
