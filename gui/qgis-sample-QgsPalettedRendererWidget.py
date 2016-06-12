# coding: utf-8
from qgis.gui import QgsPalettedRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()  # From a paletted raster
paletted_renderer_widget = QgsPalettedRendererWidget(
    layer
)

paletted_renderer_widget.show()
