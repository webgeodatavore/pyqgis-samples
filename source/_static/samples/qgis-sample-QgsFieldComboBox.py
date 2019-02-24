# coding: utf-8
from PyQt4.QtGui import QDialog, QFormLayout
from qgis.gui import (QgsFieldComboBox, QgsMapLayerComboBox,
                      QgsMapLayerProxyModel)

# Create dialog
new_dialog = QDialog()

# Add combobox for layer and field
map_layer_combo_box = QgsMapLayerComboBox()
map_layer_combo_box.setCurrentIndex(-1)
map_layer_combo_box.setFilters(QgsMapLayerProxyModel.VectorLayer)
field_combo_box = QgsFieldComboBox()

# Create a form layout and add the two combobox
layout = QFormLayout()
layout.addWidget(map_layer_combo_box)
layout.addWidget(field_combo_box)

# Add signal event
map_layer_combo_box.layerChanged.connect(field_combo_box.setLayer)  # setLayer is a native slot function


def on_field_changed(fieldName):
    print(fieldName)
    print("Layer field changed")

field_combo_box.fieldChanged.connect(on_field_changed)

new_dialog.setLayout(layout)
new_dialog.show()  # To see possibility of this component, you need at least a layer opened