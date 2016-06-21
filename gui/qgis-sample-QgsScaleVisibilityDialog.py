# coding: utf-8
from qgis.gui import QgsScaleVisibilityDialog
from qgis.utils import iface

canvas = iface.mapCanvas()
main_window = iface.mainWindow()

scale_visibility_dialog = QgsScaleVisibilityDialog(
    main_window,
    u"My visibility widget",
    canvas
)

scale_visibility_dialog.show()
