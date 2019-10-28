# coding: utf-8
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog
from qgis.gui import QgsBrushStyleComboBox

# We use the style available in brush styles.
# You may need to use the QObject tr method for translation
available_brush_styles = {
    Qt.NoBrush: "No Brush",
    Qt.HorPattern: "Horizontal",
    Qt.VerPattern: "Vertical",
    Qt.CrossPattern: "Cross",
    Qt.BDiagPattern: "BDiagonal",
    Qt.FDiagPattern: "FDiagonal",
    Qt.DiagCrossPattern: "Diagonal X",
    Qt.Dense1Pattern: "Dense 1",
    Qt.Dense2Pattern: "Dense 2",
    Qt.Dense3Pattern: "Dense 3",
    Qt.Dense4Pattern: "Dense 4",
    Qt.Dense5Pattern: "Dense 5",
    Qt.Dense6Pattern: "Dense 6",
    Qt.Dense7Pattern: "Dense 7"
}

# Create dialog and resize it
new_dialog = QDialog()
new_dialog.resize(800, 600)

brush_style_combo_box = QgsBrushStyleComboBox(new_dialog)


def on_brush_style_changed():
    print(available_brush_styles[brush_style_combo_box.brushStyle()])
    print("Brush style changed")

brush_style_combo_box.currentIndexChanged.connect(on_brush_style_changed)

new_dialog.show()
