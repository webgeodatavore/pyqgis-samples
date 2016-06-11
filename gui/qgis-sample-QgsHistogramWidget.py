# coding: utf-8
from qgis.gui import QgsHistogramWidget
from qgis.utils import iface

layer = iface.activeLayer()
histogram_widget = QgsHistogramWidget(None, layer)

histogram_widget.show()
