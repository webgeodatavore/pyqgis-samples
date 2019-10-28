# coding: utf-8
from qgis.core import QgsDropShadowEffect, QgsEffectStack
from qgis.gui import QgsEffectStackPropertiesWidget

effect_stack = QgsEffectStack(QgsDropShadowEffect())
effect_stack_properties_widget = QgsEffectStackPropertiesWidget(effect_stack)

effect_stack_properties_widget.show()
