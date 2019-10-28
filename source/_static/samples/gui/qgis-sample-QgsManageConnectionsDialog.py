# coding: utf-8
from qgis.gui import QgsManageConnectionsDialog

file_path = "/tmp/export.xml"

manage_connections_dialog_export = QgsManageConnectionsDialog(
    mode=QgsManageConnectionsDialog.Export,  # Can be Import or Export
    type=QgsManageConnectionsDialog.PostGIS,  # Could be WMS, PostGIS, WFS, MSSQL, DB2, WCS or Oracle
    fileName=file_path
)
manage_connections_dialog_export.show()

manage_connections_dialog_import = QgsManageConnectionsDialog(
    mode=QgsManageConnectionsDialog.Import,
    type=QgsManageConnectionsDialog.PostGIS,
    fileName=file_path
)
manage_connections_dialog_import.show()


manage_connections_dialog_import.selectAll()
manage_connections_dialog_import.clearSelection()
manage_connections_dialog_import.doExportImport()
manage_connections_dialog_import.selectionChanged()  # Not sure about this slot purpose
