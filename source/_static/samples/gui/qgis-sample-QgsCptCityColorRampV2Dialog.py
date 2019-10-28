# coding: utf-8
from qgis.core import QgsCptCityColorRampV2
from qgis.gui import QgsCptCityColorRampV2Dialog

cpt_city_color_ramp_v2_dialog = QgsCptCityColorRampV2Dialog(
    QgsCptCityColorRampV2()
)

cpt_city_color_ramp_v2_dialog.show()
