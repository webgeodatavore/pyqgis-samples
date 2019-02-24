# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.core import QgsVectorLayerCache
from qgis.gui import (QgsAttributeTableFilterModel, QgsAttributeTableModel,
                      QgsFeatureListModel, QgsFeatureListView,
                      QgsFeatureListViewDelegate)

from qgis.utils import iface

new_dialog = QDialog()
new_dialog.resize(270, 210)

layer = iface.activeLayer()
canvas = iface.mapCanvas()
feature_list_view = QgsFeatureListView(new_dialog)
vector_layer_cache = QgsVectorLayerCache(layer, 10000)
attribute_table_model = QgsAttributeTableModel(vector_layer_cache)
attribute_table_model.loadLayer()
attribute_table_filter_model = QgsAttributeTableFilterModel(
    canvas,
    attribute_table_model
)
feature_list_model = QgsFeatureListModel(attribute_table_filter_model)
feature_list_model.setDisplayExpression('"ADMIN"')
feature_list_view_delegate = QgsFeatureListViewDelegate(feature_list_model)
feature_list_view.setModel(feature_list_model)
# feature_list_view.setItemDelegate(feature_list_view_delegate) # Crash if uncommented. TODO: fix issue

new_dialog.show()
