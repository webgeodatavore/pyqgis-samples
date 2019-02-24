# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.gui import QgsBlendModeComboBox

new_dialog = QDialog()
new_dialog.resize(200, 200)

blend_mode_combo_box = QgsBlendModeComboBox(new_dialog)

enum_composition_mode = [
    'CompositionMode_SourceOver',
    'CompositionMode_DestinationOver',
    'CompositionMode_Clear',
    'CompositionMode_Source',
    'CompositionMode_Destination',
    'CompositionMode_SourceIn',
    'CompositionMode_DestinationIn',
    'CompositionMode_SourceOut',
    'CompositionMode_DestinationOut',
    'CompositionMode_SourceAtop',
    'CompositionMode_DestinationAtop',
    'CompositionMode_Xor',
    'CompositionMode_Plus',
    'CompositionMode_Multiply',
    'CompositionMode_Screen',
    'CompositionMode_Overlay',
    'CompositionMode_Darken',
    'CompositionMode_Lighten',
    'CompositionMode_ColorDodge',
    'CompositionMode_ColorBurn',
    'CompositionMode_HardLight',
    'CompositionMode_SoftLight',
    'CompositionMode_Difference',
    'CompositionMode_Exclusion',
    'RasterOp_SourceOrDestination',
    'RasterOp_SourceAndDestination',
    'RasterOp_SourceXorDestination',
    'RasterOp_NotSourceAndNotDestination',
    'RasterOp_NotSourceOrNotDestination',
    'RasterOp_NotSourceXorDestination',
    'RasterOp_NotSource',
    'RasterOp_NotSourceAndDestination',
    'RasterOp_SourceAndNotDestination'
]


def on_blend_mode_changed(index):
    # See enum QPainter.CompositionMode for correspondance
    print blend_mode_combo_box.blendMode()
    print 'Qpainter.' + enum_composition_mode[blend_mode_combo_box.blendMode()]

# Signal inherited from QComboBox
blend_mode_combo_box.currentIndexChanged.connect(on_blend_mode_changed)

new_dialog.show()

# Exercice: custom signal to directly emit blendMode value as a name
