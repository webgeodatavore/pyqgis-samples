# coding: utf-8
from PyQt4.QtCore import Qt
from qgis.gui import QgsSlider

slider = QgsSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setSingleStep(10)


def on_value_changed(val):
    print('azerty')
    print(val)

slider.valueChanged.connect(on_value_changed)

slider.show()
