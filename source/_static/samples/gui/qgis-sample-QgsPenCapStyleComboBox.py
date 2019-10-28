# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.gui import QgsPenCapStyleComboBox

# Create dialog and resize it
new_dialog = QDialog()
new_dialog.resize(200, 40)

pen_cap_style_combo_box = QgsPenCapStyleComboBox(new_dialog)


def on_pen_cap_style_changed():
    print(pen_cap_style_combo_box.penCapStyle())  # Value can be Qt.SquareCap, Qt.FlatCap, Qt.RoundCap
    print(pen_cap_style_combo_box.currentText())
    print("Pen cap style changed")

pen_cap_style_combo_box.currentIndexChanged.connect(on_pen_cap_style_changed)

new_dialog.show()
