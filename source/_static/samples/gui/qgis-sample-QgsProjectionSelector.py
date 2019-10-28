# coding: utf-8
from PyQt4.QtGui import QDialog, QVBoxLayout
from qgis.gui import QgsProjectionSelector

new_dialog = QDialog()
new_dialog.resize(800, 800)

layout = QVBoxLayout()

projection_selector = QgsProjectionSelector(new_dialog)  # Widget based

layout.addWidget(projection_selector)

new_dialog.setLayout(layout)

new_dialog.show()
