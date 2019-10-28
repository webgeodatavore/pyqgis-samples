# coding: utf-8
from PyQt4.QtCore import QSettings
from qgis.core import QgsApplication
from qgis.gui import QgsSvgSelectorDialog

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

svg_selector_dialog = QgsSvgSelectorDialog()
svg_selector_dialog.show()
