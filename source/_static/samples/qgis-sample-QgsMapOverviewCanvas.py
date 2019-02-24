# coding: utf-8
from PyQt4.QtCore import Qt, QObject
from PyQt4.QtGui import QColor, QVBoxLayout, QDockWidget
from qgis.gui import QgsMapOverviewCanvas
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
main_window = iface.mainWindow()

new_dock_widget = QDockWidget(u"My doc widget")

layout = QVBoxLayout()

map_canvas_overview = QgsMapOverviewCanvas(
    new_dock_widget,
    canvas
)

layerset = [layer.id()]
map_canvas_overview.setLayerSet(layerset)
map_canvas_overview.setBackgroundColor(QColor(255, 127, 0))
map_canvas_overview.enableAntiAliasing(True)
map_canvas_overview.setMinimumWidth(380)
map_canvas_overview.setMinimumHeight(280)
new_dock_widget.resize(400, 300)
layout.addWidget(map_canvas_overview)

new_dock_widget.setLayout(layout)

main_window.addDockWidget(Qt.RightDockWidgetArea, new_dock_widget)
new_dock_widget.show()

map_canvas_overview.refresh()  # Make the background color disappear?

# Layout optional playground
layout.setContentsMargins(0, 0, 0, 0)

# To clean unuseful reference widgets
# [main_window.removeDockWidget(i) for i in QObject.findChildren(main_window, QDockWidget) if i.windowTitle() == u'My doc widget']
