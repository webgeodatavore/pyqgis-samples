# coding: utf-8
from qgis.core import QgsColorSchemeRegistry, QgsCustomColorScheme
from qgis.gui import QgsColorSchemeList, QgsColorSchemeModel

color_scheme_registry = QgsColorSchemeRegistry.instance()
schemes = color_scheme_registry.schemes()
project_scheme = [s for s in schemes if isinstance(s, QgsCustomColorScheme)][0]

color_scheme_list = QgsColorSchemeList()
# Doing
color_scheme_model = QgsColorSchemeModel(project_scheme)
color_scheme_list.setModel(color_scheme_model)
# or below do the same: change color in the component
# First option is lower level when you need to reuse
# the model in another component
color_scheme_list.setScheme(project_scheme)

color_scheme_list.show()
