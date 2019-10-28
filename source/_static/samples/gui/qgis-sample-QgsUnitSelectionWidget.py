# coding: utf-8
from qgis.gui import QgsUnitSelectionWidget
from qgis.utils import iface

canvas = iface.mapCanvas()
unit_selection_widget = QgsUnitSelectionWidget()
unit_selection_widget.setMapCanvas(canvas)
# unit_selection_widget.setUnits([
# unit_selection_widget.setUnits([
#     QgsSymbolV2.MM,
#     QgsSymbolV2.Pixel,
#     QgsSymbolV2.MapUnit,
#     QgsSymbolV2.Percentage
# ]) # Bug with enum to confirm with following output message
# qgis: /build/buildd/sip4-4.15.5/siplib/siplib.c:8407:
# sip_api_can_convert_to_type:  Assertion `(((td)->td_flags & 0x0007) == 0x0000) || (((td)->td_flags & 0x0007) == 0x0002)' failed.

unit_selection_widget.resize(400, 30)

unit_selection_widget.show()
