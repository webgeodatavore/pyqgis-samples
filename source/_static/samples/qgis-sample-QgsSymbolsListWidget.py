# coding: utf-8
from PyQt4.QtGui import QMenu
from qgis.core import QgsStyleV2
from qgis.gui import QgsSymbolsListWidget
from qgis.utils import iface

layer = iface.activeLayer()
symbols_list_widget = QgsSymbolsListWidget(
    layer.rendererV2().symbol(),
    QgsStyleV2.defaultStyle(),
    QMenu(),
    None,
    layer
)

symbols_list_widget.show()
