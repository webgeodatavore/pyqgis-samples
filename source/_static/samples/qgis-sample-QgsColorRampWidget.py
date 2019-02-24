# coding: utf-8
from qgis.gui import QgsColorRampWidget, QgsColorWidget

color_ramp_widget = QgsColorRampWidget(
    None,
    QgsColorWidget.Hue,  # Can be Multiple, Red, Green, Blue, Hue, Saturation, Value, Alpha
    QgsColorRampWidget.Vertical  # Horizontal by default
)
color_ramp_widget.resize(50, 100)

color_ramp_widget.setInteriorMargin(5)
color_ramp_widget.setShowFrame(False)

print(
    color_ramp_widget.color().red(),
    color_ramp_widget.color().green(),
    color_ramp_widget.color().blue()
)
print(color_ramp_widget.component())
print(color_ramp_widget.componentValue())

color_ramp_widget.show()
