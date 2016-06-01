# coding: utf-8
from qgis.gui import QgsEncodingFileDialog
from qgis.utils import iface

encoding_file_dialog = QgsEncodingFileDialog(
    iface.mainWindow(),
    caption=u"Nom de la fenêtre",
    directory="mon_fichier.txt",
    filter="Texte (*.txt *.csv)",
    encoding="utf-8"
)

encoding_file_dialog.setNameFilters(
    ['Jpeg (*.jpg *.jpeg)',
     'Texte (*.txt *.csv)']
)
encoding_file_dialog.show()
