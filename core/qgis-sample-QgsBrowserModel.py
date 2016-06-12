# coding: utf-8
from qgis.core import QgsBrowserModel
from qgis.gui import QgsBrowserTreeView

browserTreeView = QgsBrowserTreeView()
browserModel = QgsBrowserModel()
browserTreeView.setModel(browserModel)

browserTreeView.show()
