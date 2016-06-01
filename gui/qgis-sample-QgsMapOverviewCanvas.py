# coding: utf-8
from PyQt4.QtCore import Qt, QObject
from PyQt4.QtGui import QColor, QDialog, QVBoxLayout, QDockWidget
from qgis.gui import QgsMapOverviewCanvas
from qgis.utils import iface

new_dialog = QDialog()
new_dialog.resize(800, 600)

new_dock_widget = QDockWidget(u"My doc widget")

layout = QVBoxLayout()

map_canvas_overview = QgsMapOverviewCanvas(
    new_dock_widget,
    iface.mapCanvas()
)

layerset = [iface.activeLayer().id()]
map_canvas_overview.setLayerSet(layerset)
map_canvas_overview.setBackgroundColor(QColor(255, 127, 0))
map_canvas_overview.enableAntiAliasing(True)
map_canvas_overview.setMinimumWidth(380)
map_canvas_overview.setMinimumHeight(280)
new_dock_widget.resize(400, 300)
layout.addWidget(map_canvas_overview)

new_dock_widget.setLayout(layout)

iface.mainWindow().addDockWidget(Qt.RightDockWidgetArea, new_dock_widget)
new_dock_widget.show()

map_canvas_overview.refresh()  # Make the background color disappear?

# Layout optional playground
layout.setContentsMargins(0, 0, 0, 0)

# To clean unuseful reference widgets
[iface.mainWindow().removeDockWidget(i) for i in QObject.findChildren(iface.mainWindow(), QDockWidget) if i.windowTitle() == u'My doc widget']
