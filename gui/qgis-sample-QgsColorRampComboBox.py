# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.core import QgsStyleV2
from qgis.gui import QgsColorRampComboBox

# Create dialog and resize it
new_dialog = QDialog()
new_dialog.resize(800, 600)

style = QgsStyleV2().defaultStyle()

color_ramp_combo_box = QgsColorRampComboBox(new_dialog)
color_ramp_combo_box.populate(style)


def on_color_ramp_changed():
    print(color_ramp_combo_box.currentColorRamp())
    print(color_ramp_combo_box.currentText())
    print("Color ramp changed")

color_ramp_combo_box.currentIndexChanged.connect(on_color_ramp_changed)

new_dialog.show()
