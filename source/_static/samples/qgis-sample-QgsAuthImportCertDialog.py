# coding: utf-8
from qgis.gui import QgsAuthImportCertDialog

auth_import_cert_dialog = QgsAuthImportCertDialog(
    None,  # The first arg is the parent widget if any wanted
    QgsAuthImportCertDialog.NoFilter,  # NoFilter or CaFilter
    QgsAuthImportCertDialog.TextInput  # AllInputs, FileInput or TextInput
)

auth_import_cert_dialog.show()
