# coding: utf-8
from qgis.core import QgsVectorRandomColorRampV2
from qgis.gui import QgsVectorRandomColorRampV2Dialog

vector_random_color_ramp_v2_dialog = QgsVectorRandomColorRampV2Dialog(
    QgsVectorRandomColorRampV2()
)

vector_random_color_ramp_v2_dialog.show()
