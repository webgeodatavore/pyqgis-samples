# coding: utf-8
from qgis.gui import QgsGroupWMSDataDialog

# Instanciate the dialog
group_wms_data_dialog = QgsGroupWMSDataDialog()

# Set data in upcoming text content
group_wms_data_dialog.setGroupAbstract('Abstract\nThis is an abstract')
group_wms_data_dialog.setGroupShortName('ShortName')
group_wms_data_dialog.setGroupTitle('Title')

# Show dialog and change content
group_wms_data_dialog.show()

# Then display changed content
print(group_wms_data_dialog.groupAbstract())
print(group_wms_data_dialog.groupShortName())
print(group_wms_data_dialog.groupTitle())
