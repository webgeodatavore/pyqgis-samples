# coding: utf-8
from qgis.core import QgsColorSchemeRegistry, QgsCustomColorScheme
from qgis.gui import QgsColorSwatchGrid

color_scheme_registry = QgsColorSchemeRegistry.instance()
schemes = color_scheme_registry.schemes()
project_scheme = [s for s in schemes if isinstance(s, QgsCustomColorScheme)][0]

color_swatch_grid = QgsColorSwatchGrid(project_scheme)

color_swatch_grid.show()
