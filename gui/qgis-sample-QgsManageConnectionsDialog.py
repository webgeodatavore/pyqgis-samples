# coding: utf-8
from qgis.gui import QgsManageConnectionsDialog

manage_connections_dialog = QgsManageConnectionsDialog(
    mode=QgsManageConnectionsDialog.Export,  # Can be Import or Export
    type=QgsManageConnectionsDialog.PostGIS,  # Could be WMS, PostGIS, WFS, MSSQL, DB2, WCS or Oracle 
    fileName="export.xml"
)
manage_connections_dialog.show()

manage_connections_dialog = QgsManageConnectionsDialog(
    mode=QgsManageConnectionsDialog.Import,
    type=QgsManageConnectionsDialog.PostGIS,
    fileName="export.xml"
)
manage_connections_dialog.show()


manage_connections_dialog.selectAll()
manage_connections_dialog.clearSelection()
manage_connections_dialog.doExportImport()
manage_connections_dialog.selectionChanged()  # Not sure about this slot purpose
