# coding: utf-8
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog, QDockWidget
from qgis.gui import QgsColorBox, QgsColorWidget
from qgis.utils import iface

new_dialog = QDialog()
new_dialog.resize(200, 200)

color_box = QgsColorBox(new_dialog)


def print_qcolor(qcolor):
    print(qcolor.name())

# Signal inherited from QgsColorWidget
color_box.colorChanged.connect(print_qcolor)

new_dialog.show()

# Change color you want to choose
color_box.setComponent(QgsColorWidget.Blue)

color_box.resize(100, 100)

# Exercice
# Change again the color you can choose.
# Where can you find the available keywords?

# There is a anormal behaviour in the boxes size.
# Try to find out which one?

# Play with QDockWidget
dock = QDockWidget()
iface.addDockWidget(Qt.RightDockWidgetArea, dock)

dock.setWidget(color_box)

new_dialog.destroy()
