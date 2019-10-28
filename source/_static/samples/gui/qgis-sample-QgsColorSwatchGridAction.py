# coding: utf-8
from PyQt4.QtGui import QDialog, QMenu, QMenuBar, QVBoxLayout
from qgis.core import QgsColorSchemeRegistry, QgsCustomColorScheme
from qgis.gui import QgsColorSwatchGridAction

new_dialog = QDialog()
main_layout = QVBoxLayout()
menu_bar = QMenuBar()
menu = QMenu(u"Test")

color_scheme_registry = QgsColorSchemeRegistry.instance()
schemes = color_scheme_registry.schemes()
project_scheme = [s for s in schemes if isinstance(s, QgsCustomColorScheme)][0]

color_swatch_grid_action = QgsColorSwatchGridAction(project_scheme, menu)

menu.addAction(color_swatch_grid_action)

menu_bar.addMenu(menu)
main_layout.setMenuBar(menu_bar)
new_dialog.setLayout(main_layout)

new_dialog.show()
