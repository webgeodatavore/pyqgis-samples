# coding: utf-8
from qgis.core import QgsEffectStack
from qgis.gui import QgsEffectStackPropertiesDialog

effect_stack = QgsEffectStack()
effect_stack_properties_dialog = QgsEffectStackPropertiesDialog(effect_stack)

effect_stack_properties_dialog.show()
