# coding: utf-8
from qgis.gui import QgsDetailedItemData, QgsDetailedItemWidget

detailed_item_widget = QgsDetailedItemWidget()
detailed_item_widget.resize(300, 240)

detailed_item_data = QgsDetailedItemData()
detailed_item_data.setCategory('myCategory')
detailed_item_data.setCheckable(True)
detailed_item_data.setChecked(True)
detailed_item_data.setDetail('myDetail')
detailed_item_data.setEnabled(True)
detailed_item_data.setTitle('myTitle')

detailed_item_widget.setData(detailed_item_data)

detailed_item_widget.show()
