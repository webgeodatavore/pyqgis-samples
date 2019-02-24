# coding: utf-8
from qgis.core import QgsDropShadowEffect
from qgis.gui import QgsEffectStackCompactWidget

effect_stack_compact_widget = QgsEffectStackCompactWidget(
    None,
    QgsDropShadowEffect()
)
effect_stack_compact_widget.resize(200, 50)

effect_stack_compact_widget.show()
