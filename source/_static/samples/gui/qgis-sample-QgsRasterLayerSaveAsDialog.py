# coding: utf-8
from qgis.gui import QgsRasterLayerSaveAsDialog
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
canvas_crs = canvas.mapSettings().destinationCrs()
raster_layer_save_as_dialog = QgsRasterLayerSaveAsDialog(
    layer,
    layer.dataProvider(),
    canvas.extent(),
    layer.crs(),
    canvas_crs
)


def on_accepted():
    print("OK")
    print(raster_layer_save_as_dialog.addToCanvas())
    print(raster_layer_save_as_dialog.buildPyramidsFlag())
    print(raster_layer_save_as_dialog.createOptions())
    print(raster_layer_save_as_dialog.maximumTileSizeX())
    print(raster_layer_save_as_dialog.maximumTileSizeY())
    print(raster_layer_save_as_dialog.mode())
    print(raster_layer_save_as_dialog.nColumns())
    print(raster_layer_save_as_dialog.noData())
    print(raster_layer_save_as_dialog.nRows())
    print(raster_layer_save_as_dialog.outputCrs())
    print(raster_layer_save_as_dialog.outputFileName())
    print(raster_layer_save_as_dialog.outputFormat())
    print(raster_layer_save_as_dialog.outputRectangle())
    print(raster_layer_save_as_dialog.pyramidsConfigOptions())
    print(raster_layer_save_as_dialog.pyramidsFormat())
    print(raster_layer_save_as_dialog.pyramidsList())
    print(raster_layer_save_as_dialog.pyramidsResamplingMethod())
    print(raster_layer_save_as_dialog.tileMode())
    print(raster_layer_save_as_dialog.xResolution())
    print(raster_layer_save_as_dialog.yResolution())
    # print(raster_layer_save_as_dialog.ideFormat()) # If you need to hide format
    # print(raster_layer_save_as_dialog.hideOutput()) # If you need to hide output

raster_layer_save_as_dialog.accepted.connect(on_accepted)

raster_layer_save_as_dialog.show()
