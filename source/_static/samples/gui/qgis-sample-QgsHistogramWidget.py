# coding: utf-8
from qgis.gui import QgsHistogramWidget
from qgis.utils import iface

layer = iface.activeLayer()
# Data matching the histogram field comes from
# http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
histogram_widget = QgsHistogramWidget(None, layer, 'POP_EST')

histogram_widget.show()
