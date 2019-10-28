# coding: utf-8
from PyQt4.QtGui import QWidget
from qgis.gui import QgsExpressionBuilderWidget

w = QWidget()
expression_builder_widget = QgsExpressionBuilderWidget(w)

w.show()
