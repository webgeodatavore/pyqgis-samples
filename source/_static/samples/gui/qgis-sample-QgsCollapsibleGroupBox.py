# coding: utf-8
from PyQt4.QtCore import QRect
from PyQt4.QtGui import (QDialog, QFrame, QLineEdit, QScrollArea,
                         QSizePolicy, QVBoxLayout, QWidget)
from qgis.gui import QgsCollapsibleGroupBox

new_dialog = QDialog()
new_dialog.resize(200, 100)

scroll_area = QScrollArea(new_dialog)
scroll_area.setFrameShape(QFrame.NoFrame)
scroll_area.setFrameShadow(QFrame.Plain)
scroll_area.setWidgetResizable(True)
scroll_area.setGeometry(QRect(10, 20, 170, 70))

scrollAreaWidgetContents = QWidget()
scrollAreaWidgetContents.setGeometry(QRect(0, 0, 170, 70))
vertical_layout = QVBoxLayout(scrollAreaWidgetContents)

collapsible_group_box = QgsCollapsibleGroupBox(scrollAreaWidgetContents)
collapsible_group_box.setTitle('Collapsible')
sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(
    collapsible_group_box.sizePolicy().hasHeightForWidth()
)
collapsible_group_box.setSizePolicy(sizePolicy)
collapsible_group_box.setChecked(False)

vbox_layout = QVBoxLayout(collapsible_group_box)
line_edit = QLineEdit(collapsible_group_box)
line_edit.setGeometry(QRect(10, 20, 110, 30))

vertical_layout.addWidget(collapsible_group_box)
scroll_area.setWidget(scrollAreaWidgetContents)

new_dialog.show()
