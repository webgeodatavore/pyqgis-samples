# coding: utf-8
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog
from qgis.gui import QgsPenStyleComboBox

# Create dialog and resize it
new_dialog = QDialog()
new_dialog.resize(200, 60)

pen_style_combo_box = QgsPenStyleComboBox(new_dialog)


def on_pen_changed():
    print(pen_style_combo_box.penStyle())  # Value can be Qt.SolidLine, Qt.NoPen, Qt.DashLine, Qt.DotLine, Qt.DashDotLine or Qt.DashDotDotLine
    print(pen_style_combo_box.currentText())
    print("Pen style changed")

pen_style_combo_box.currentIndexChanged.connect(on_pen_changed)

new_dialog.show()
