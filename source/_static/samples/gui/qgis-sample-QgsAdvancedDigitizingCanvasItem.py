from qgis.gui import (QgsAdvancedDigitizingCanvasItem,
    QgsAdvancedDigitizingDockWidget)
from qgis.utils import iface

canvas = iface.mapCanvas()
dock = QgsAdvancedDigitizingDockWidget(canvas)

iface.addDockWidget(Qt.RightDockWidgetArea, dock)
QgsAdvancedDigitizingCanvasItem(canvas, dock)
