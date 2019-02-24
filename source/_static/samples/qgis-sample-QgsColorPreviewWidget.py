# coding: utf-8
from PyQt4.QtGui import QColor
from qgis.gui import QgsColorPreviewWidget, QgsColorWidget

color_preview_widget = QgsColorPreviewWidget()
current_color = QColor('#237adf')
preview_color = QColor('#986a8c')
color_preview_widget.setColor(current_color)  # Set current color
color_preview_widget.setColor2(preview_color)  # Set preview color

# Can be Multiple, Red, Green, Blue, Hue, Saturation, Value, Alpha
print(color_preview_widget.componentValue(QgsColorWidget.Red))
print(color_preview_widget.componentValue(QgsColorWidget.Green))
print(color_preview_widget.componentValue(QgsColorWidget.Blue))

color_preview_widget.resize(70, 50)

color_preview_widget.show()
