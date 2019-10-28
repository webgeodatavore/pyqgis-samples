# coding: utf-8
from qgis.core import QgsBrowserModel
from qgis.gui import QgsBrowserTreeView

browser_tree_view = QgsBrowserTreeView()
browser_model = QgsBrowserModel()
browser_tree_view.setModel(browser_model)

browser_tree_view.show()
