# coding: utf-8
from qgis.gui import QgsGraduatedHistogramWidget
from qgis.utils import iface

layer = iface.activeLayer()
graduated_histogram_widget = QgsGraduatedHistogramWidget()
graduated_histogram_widget.setRenderer(layer.rendererV2())
graduated_histogram_widget.setLayer(layer)

graduated_histogram_widget.show()
