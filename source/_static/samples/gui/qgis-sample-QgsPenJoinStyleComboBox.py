# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.gui import QgsPenJoinStyleComboBox

# Create dialog and resize it
new_dialog = QDialog()
new_dialog.resize(200, 40)

pen_join_style_combo_box = QgsPenJoinStyleComboBox(new_dialog)


def on_pen_join_changed():
    print(pen_join_style_combo_box.penJoinStyle())  # Value can be Qt.BevelJoin, Qt.MiterJoin, Qt.RoundJoin
    print(pen_join_style_combo_box.currentText())
    print("Pen join style changed")

pen_join_style_combo_box.currentIndexChanged.connect(on_pen_join_changed)

new_dialog.show()
