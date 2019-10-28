# coding: utf-8
from qgis.core import QgsStyleV2
from qgis.gui import QgsStyleV2ExportImportDialog

style_v2_export_import_dialog = QgsStyleV2ExportImportDialog(
    QgsStyleV2.defaultStyle()
)

style_v2_export_import_dialog.show()
