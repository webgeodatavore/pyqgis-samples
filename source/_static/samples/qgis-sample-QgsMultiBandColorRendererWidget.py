# coding: utf-8
from qgis.gui import QgsMultiBandColorRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()  # From a multiband raster
multi_band_color_renderer_widget = QgsMultiBandColorRendererWidget(
    layer
)

multi_band_color_renderer_widget.show()
