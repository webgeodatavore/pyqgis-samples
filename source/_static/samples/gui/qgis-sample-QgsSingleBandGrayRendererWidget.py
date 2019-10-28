# coding: utf-8
from qgis.gui import QgsSingleBandGrayRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()

single_band_gray_renderer_widget = QgsSingleBandGrayRendererWidget(
    layer
)

single_band_gray_renderer_widget.show()
