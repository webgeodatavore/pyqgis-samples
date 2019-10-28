# coding: utf-8
from qgis.gui import QgsEncodingFileDialog
from qgis.utils import iface

main_window = iface.mainWindow()
encoding_file_dialog = QgsEncodingFileDialog(
    main_window,
    caption=u"Window name",
    directory="myfilename.txt",
    filter="Text (*.txt *.csv)",
    encoding="utf-8"
)

encoding_file_dialog.setNameFilters(
    ['Jpeg (*.jpg *.jpeg)',
     'Texte (*.txt *.csv)']
)
encoding_file_dialog.show()
