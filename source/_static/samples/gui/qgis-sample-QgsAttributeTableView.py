# coding: utf-8
from PyQt4.QtGui import QTableView
from qgis.core import QgsVectorLayerCache
from qgis.gui import (QgsAttributeTableModel,
                      QgsAttributeTableView,
                      QgsAttributeTableFilterModel)
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
vector_layer_cache = QgsVectorLayerCache(layer, 10000)
attribute_table_model = QgsAttributeTableModel(vector_layer_cache)
attribute_table_model.loadLayer()

attribute_table_filter_model = QgsAttributeTableFilterModel(
    canvas,
    attribute_table_model
)
attribute_table_view = QgsAttributeTableView()
attribute_table_view.setModel(attribute_table_filter_model)

attribute_table_view.show()

# Or display the attribute_table_model with QTableView (pure QT solution)
table_view = QTableView()
table_view.setModel(attribute_table_model)
table_view.show()
