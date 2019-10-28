# coding: utf-8
from PyQt4.QtGui import QDialog, QTableView
from qgis.core import QgsVectorLayerCache
from qgis.gui import (QgsAttributeTableModel,
                      QgsAttributeTableView,
                      QgsAttributeTableFilterModel)
from qgis.utils import iface

new_dialog = QDialog()
new_dialog.resize(800, 600)

vector_layer_cache = QgsVectorLayerCache(iface.activeLayer(), 10000)
attribute_table_model = QgsAttributeTableModel(vector_layer_cache)
attribute_table_model.loadLayer()

attribute_table_filter_model = QgsAttributeTableFilterModel(
    iface.mapCanvas(),
    attribute_table_model
)
attribute_table_view = QgsAttributeTableView(new_dialog)
attribute_table_view.setModel(attribute_table_filter_model)

new_dialog.show()

# Or display the attribute_table_model with QTableView (pure QT solution)
table_view = QTableView()
table_view.setModel(attribute_table_model)
table_view.show()
