# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.core import QgsPaintEffect
from qgis.gui import QgsEffectDrawModeComboBox

# Create dialog and resize it
new_dialog = QDialog()
new_dialog.resize(250, 75)

effect_draw_mode_combo_box = QgsEffectDrawModeComboBox(new_dialog)


def on_effect_draw_mode_changed():
    print([
        i for i in ['Modifier', 'Render', 'ModifyAndRender']
        if (effect_draw_mode_combo_box.drawMode() == getattr(QgsPaintEffect, i))
    ][0])
    print(effect_draw_mode_combo_box.drawMode())
    print("Effect draw mode changed")

effect_draw_mode_combo_box.currentIndexChanged.connect(on_effect_draw_mode_changed)

new_dialog.show()

# You should disconnect events when you play with signals and slots e.g:
# effect_draw_mode_combo_box.currentIndexChanged.disconnect(on_effect_draw_mode_changed)
