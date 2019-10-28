# coding: utf-8
from qgis.gui import QgsSingleBandPseudoColorRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()
single_band_pseudo_color_renderer_widget = QgsSingleBandPseudoColorRendererWidget(
    layer
)

single_band_pseudo_color_renderer_widget.show()
