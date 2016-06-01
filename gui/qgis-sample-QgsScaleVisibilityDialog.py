# coding: utf-8
from qgis.gui import QgsScaleVisibilityDialog
from qgis.utils import iface

scale_visibility_dialog = QgsScaleVisibilityDialog(
    iface.mainWindow(),
    u"My visibility widget",
    iface.mapCanvas()
)
scale_visibility_dialog.show()
