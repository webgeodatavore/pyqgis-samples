# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.gui import QgsScaleComboBox
from qgis.utils import iface

new_dialog = QDialog()
new_dialog.resize(150, 50)

scale_box = QgsScaleComboBox(new_dialog)


def on_scale_changed():
    print(scale_box.scale(),
          QgsScaleComboBox.toString(scale_box.scale()))
    print(scale_box.scaleString(),
          QgsScaleComboBox.toDouble(scale_box.scaleString()))
    print("Scale changed")
    iface.mapCanvas().zoomScale(1 / scale_box.scale())

# The default values come from Options > Cartographic Tools, part Predefined scales
all_scales = [scale_box.itemText(i) for i in range(scale_box.count())]

scale_box.scaleChanged.connect(on_scale_changed)

new_dialog.show()

scale_box.updateScales([u'1:1\xa0000\xa0000', u'1:100\xa0000'])
