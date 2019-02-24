# coding: utf-8
from PyQt4.QtGui import QDialog
from qgis.gui import QgsScaleWidget
from qgis.utils import iface

new_dialog = QDialog()
new_dialog.resize(150, 50)

scale_widget = QgsScaleWidget(new_dialog)


def on_scale_changed():
    print(scale_widget.scale(),
          QgsScaleWidget.toString(scale_widget.scale()))
    print(scale_widget.scaleString(),
          QgsScaleWidget.toDouble(scale_widget.scaleString()))
    print(scale_widget.showCurrentScaleButton())
    print("Scale changed")
    iface.mapCanvas().zoomScale(1 / scale_widget.scale())

scale_widget.scaleChanged.connect(on_scale_changed)

new_dialog.show()

scale_widget.updateScales([u'1:1\xa0000\xa0000', u'1:100\xa0000'])
