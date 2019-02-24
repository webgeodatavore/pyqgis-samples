# coding: utf-8
from qgis.core import QgsVectorGradientColorRampV2
from qgis.gui import QgsVectorGradientColorRampV2Dialog

vector_gradient_color_ramp_v2_dialog = QgsVectorGradientColorRampV2Dialog(
    QgsVectorGradientColorRampV2()
)
vector_gradient_color_ramp_v2_dialog.show()
