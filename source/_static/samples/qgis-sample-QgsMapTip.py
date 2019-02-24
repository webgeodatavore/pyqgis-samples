# coding: utf-8
from PyQt4.QtCore import QTimer
from qgis.core import QgsPoint
from qgis.gui import QgsMapTip
from qgis.utils import iface


class ToolTip:
    def __init__(self, canvas, layer=None):
        self.canvas = canvas
        self.layer = layer

    def createMapTips(self):
        """ Create MapTips on the map """
        self.timer_map_tips = QTimer(self.canvas)
        self.map_tip = QgsMapTip()
        self.canvas.xyCoordinates.connect(self.mapTipXYChanged)
        self.timer_map_tips.timeout.connect(self.showMapTip)

    def mapTipXYChanged(self, p):
        """ SLOT. Initialize the Timer to show MapTips on the map """
        if self.canvas.underMouse():  # Only if mouse is over the map
            # Here you could check if your custom MapTips button is active
            self.lastMapPosition = QgsPoint(p.x(), p.y())
            self.map_tip.clear(self.canvas)
            self.timer_map_tips.start(750)  # time in milliseconds

    def showMapTip(self):
        """ SLOT. Show  MapTips on the map """
        self.timer_map_tips.stop()

        if self.canvas.underMouse():
            # Here you could check if your custom MapTips button is active
            point_qgs = self.lastMapPosition
            point_qt = self.canvas.mouseLastXY()
            if self.layer:
                self.map_tip.showMapTip(
                    self.layer,
                    point_qgs,
                    point_qt,
                    self.canvas
                )
            else:
                print "You should set a layer"


canvas = iface.mapCanvas()
layer = iface.activeLayer()
my_tool_tip = ToolTip()
my_tool_tip.createMapTips()
my_tool_tip.layer = layer
my_tool_tip.layer.setDisplayField('NAME_LONG')
my_tool_tip.layer.setDisplayField('NAME')

# Exercice: add to manage disconnect
