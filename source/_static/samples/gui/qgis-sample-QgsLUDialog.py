# coding: utf-8
from qgis.gui import QgsLUDialog

lower_upper_dialog = QgsLUDialog()
lower_upper_dialog.show()

lower_upper_dialog.lowerValue()  # Matching setter setLowerValue
lower_upper_dialog.upperValue()  # Matching setter setUpperValue
