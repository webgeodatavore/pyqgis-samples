# Make your own signal
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QDialog
from qgis.gui import QgsBlendModeComboBox

new_dialog = QDialog()
new_dialog.resize(200, 200)


class QgsBlendModeComboBoxWithCustomSignal(QgsBlendModeComboBox):
    onBlendChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        # Initialize the QgsBlendModeComboBoxWithCustomSignal as a QgsBlendModeComboBox
        QgsBlendModeComboBox.__init__(self, parent)
        self.currentIndexChanged.connect(self._onBlendChanged)

    def _onBlendChanged(self):
        self.onBlendChanged.emit(self.blendMode())

blend_mode_combo_box = QgsBlendModeComboBoxWithCustomSignal(new_dialog)

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


def print_blend_mode(index):
    # See enum QPainter.CompositionMode for correspondance
    print enum_composition_mode[index]

# Custom signal from QgsBlendModeComboBoxWithCustomSignal
blend_mode_combo_box.onBlendChanged.connect(print_blend_mode)

new_dialog.show()