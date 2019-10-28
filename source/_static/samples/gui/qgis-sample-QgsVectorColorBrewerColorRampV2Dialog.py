# coding: utf-8
from qgis.core import QgsVectorColorBrewerColorRampV2
from qgis.gui import QgsVectorColorBrewerColorRampV2Dialog

vector_color_brewer_color_ramp_v2_dialog = QgsVectorColorBrewerColorRampV2Dialog(
    QgsVectorColorBrewerColorRampV2()
)

vector_color_brewer_color_ramp_v2_dialog.show()
