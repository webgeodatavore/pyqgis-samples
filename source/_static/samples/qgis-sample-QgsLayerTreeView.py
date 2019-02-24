# coding: utf-8
from qgis.core import QgsProject, QgsLayerTreeModel
from qgis.gui import QgsLayerTreeView

root = QgsProject.instance().layerTreeRoot()
model = QgsLayerTreeModel(root)
view = QgsLayerTreeView()
view.setModel(model)
view.show()
