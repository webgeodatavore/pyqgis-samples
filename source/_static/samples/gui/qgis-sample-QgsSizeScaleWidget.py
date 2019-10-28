# coding: utf-8
from qgis.core import QgsMarkerSymbolV2
from qgis.gui import QgsSizeScaleWidget
from qgis.utils import iface


layer = iface.activeLayer()
canvas = iface.mapCanvas()
marker_symbol_v2 = QgsMarkerSymbolV2.createSimple({
    'color': 'blue',
    'name': 'triangle'
})

size_scale_widget = QgsSizeScaleWidget(layer, marker_symbol_v2)
size_scale_widget.setMapCanvas(canvas)

size_scale_widget.show()
