# coding: utf-8
from qgis.core import QgsCoordinateReferenceSystem
from qgis.gui import QgsProjectionSelectionWidget

projection_selection_widget = QgsProjectionSelectionWidget()
projection_selection_widget.resize(400, 30)
projection_selection_widget.setCrs(QgsCoordinateReferenceSystem('EPSG:4326'))

projection_selection_widget.show()
