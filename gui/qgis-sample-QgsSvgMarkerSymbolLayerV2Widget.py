# coding: utf-8
from PyQt4.QtCore import QSettings
from qgis.core import QgsApplication
from qgis.gui import QgsSvgMarkerSymbolLayerV2Widget
from qgis.utils import iface

# Print the SVG paths
print(QgsApplication.svgPaths())

# Specific to our use case.
# QgsApplication.setDefaultSvgPaths did not alter all the paths.
# Default value for "svg/searchPathsForSVG" is $HOME but as we had many git
# repositories under $HOME, QGIS was scanning all of them to look for SVG.
# Uncomment or not depending of your case
# s = QSettings()
# s.setValue("svg/searchPathsForSVG", "/tmp")  # Change the path if on Windows

# To confirm the difference if you apply above two previous lines
print(QgsApplication.svgPaths())

layer = iface.activeLayer()
svg_marker_symbol_layer_v2_widget = QgsSvgMarkerSymbolLayerV2Widget(layer)
svg_marker_symbol_layer_v2_widget.show()
