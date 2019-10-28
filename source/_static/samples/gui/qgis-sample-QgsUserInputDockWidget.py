# coding: utf-8
from PyQt4.QtCore import Qt
from qgis.core import QgsCoordinateReferenceSystem
from qgis.gui import QgsUserInputDockWidget, QgsProjectionSelectionWidget
from qgis.utils import iface

projection_selection_widget = QgsProjectionSelectionWidget()
projection_selection_widget.resize(400, 30)
projection_selection_widget.setCrs(QgsCoordinateReferenceSystem('EPSG:4326'))

user_input_dock_widget = QgsUserInputDockWidget()
user_input_dock_widget.addUserInputWidget(projection_selection_widget)

iface.addDockWidget(Qt.RightDockWidgetArea, user_input_dock_widget)
# iface.removeDockWidget(user_input_dock_widget)
