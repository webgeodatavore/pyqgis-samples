# coding: utf-8
from qgis.core import QgsBlurEffect
from qgis.gui import QgsTransformWidget

transform_widget = QgsTransformWidget()
transform_widget.setPaintEffect(QgsBlurEffect())

transform_widget.show()
