# coding: utf-8
from PyQt4.QtGui import QDialog, QVBoxLayout
from qgis.gui import QgsColorButton

# Create dialog and widget
d = QDialog()
# Create the color button
color_button = QgsColorButton()

# Create layout and add the button as a widget to it
vbox = QVBoxLayout()
vbox.addWidget(color_button)

# Set the dialog layout
d.setLayout(vbox)

# Show the dialog and hence, the QgsColorButtonV2
d.show()
