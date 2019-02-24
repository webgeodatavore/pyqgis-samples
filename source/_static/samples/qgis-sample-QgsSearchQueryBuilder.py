# coding: utf-8
from qgis.gui import QgsSearchQueryBuilder
from qgis.utils import iface

layer = iface.activeLayer()
search_query_builder = QgsSearchQueryBuilder(layer)

search_query_builder.show()
