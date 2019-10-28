# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.gui import QgsFilterLineEdit

new_dialog = QDialog()
new_dialog.resize(165, 40)
file_widget = QgsFilterLineEdit(new_dialog)

new_dialog.show()
