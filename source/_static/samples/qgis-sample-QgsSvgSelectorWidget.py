# coding: utf-8
from PyQt4.QtCore import QSettings
from qgis.core import QgsApplication
from qgis.gui import QgsSvgSelectorWidget

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

svg_selector_widget = QgsSvgSelectorWidget()
svg_selector_widget.show()


def on_svg_selected(path):
    print(path)

# Signal
svg_selector_widget.svgSelected.connect(on_svg_selected)

# Functions
print(svg_selector_widget.currentSvgPath())  # Path in the current bottom left QLineEdit
svg_path = '/tmp'
svg_selector_widget.setSvgPath(svg_path)  # Setter for the above path
print(svg_selector_widget.currentSvgPathToName())
print(svg_selector_widget.filePathButton())  # QPushButton at the bottom

print(svg_selector_widget.filePathLineEdit())  # QLineEdit at the bottom on the left
print(svg_selector_widget.groupsTreeView())  # QTreeView in the left panel to display path tree
print(svg_selector_widget.imagesListView())  # QListView in the right panel, to display svg images
print(svg_selector_widget.relativePathCheckbox())  # QCheckBox in the bottom right
print(svg_selector_widget.selectorLayout())  # QLayout
