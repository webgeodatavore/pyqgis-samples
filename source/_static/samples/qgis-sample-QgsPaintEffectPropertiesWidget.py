# coding: utf-8
from qgis.core import QgsDropShadowEffect
from qgis.gui import QgsPaintEffectPropertiesWidget

paint_effect_properties_widget = QgsPaintEffectPropertiesWidget(
    QgsDropShadowEffect()
)

paint_effect_properties_widget.show()
