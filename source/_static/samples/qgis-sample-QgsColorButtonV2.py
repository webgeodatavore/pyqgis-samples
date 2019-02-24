# coding: utf-8
from PyQt4.QtGui import QDialog, QVBoxLayout
from qgis.gui import QgsColorButtonV2

# Create dialog and widget
d = QDialog()
# Create the color button
btn = QgsColorButtonV2()

# Create layout and add the button as a widget to it
vbox = QVBoxLayout()
vbox.addWidget(btn)

# Set the dialog layout
d.setLayout(vbox)

# Show the dialog and hence, the QgsColorButtonV2
d.show()
