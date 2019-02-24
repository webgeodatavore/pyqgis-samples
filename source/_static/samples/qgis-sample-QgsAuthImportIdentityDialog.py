# coding: utf-8
from qgis.gui import QgsAuthImportIdentityDialog

auth_import_identity_dialog = QgsAuthImportIdentityDialog(
    QgsAuthImportIdentityDialog.IdentityType(),
    None
)

auth_import_identity_dialog.show()
