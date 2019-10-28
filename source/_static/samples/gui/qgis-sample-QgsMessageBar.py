# coding: utf-8
"""All credits here go to the official cookbook for
this class documentation samples at
http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/communicating.html.
"""

import time
from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QProgressBar, QPushButton, QDialog,
                         QSizePolicy, QGridLayout, QDialogButtonBox)
from qgis.utils import iface
from qgis.gui import QgsMessageBar

# Get QGIS existing QqsMessageBar
iface.messageBar().pushInfo(u'My Plugin says', u'Hey there')
iface.messageBar().pushMessage(
    "Error",
    "Please select a Topographic Map for your simulation!",
    QgsMessageBar.CRITICAL,
    2
)

# Widgets can be added to the message bar,
# like for instance a button to show more info


def showError():
    pass

widget = iface.messageBar().createMessage("Missing Layers", "Show Me")
button = QPushButton(widget)
button.setText("Show Me")
button.pressed.connect(showError)
widget.layout().addWidget(button)
iface.messageBar().pushWidget(widget, QgsMessageBar.WARNING)

# You can even use a message bar in your own dialog so you don’t have to show
# a message box, or if it doesn’t make sense to show it in the main QGIS window


class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.bar = QgsMessageBar()
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonbox.accepted.connect(self.run)
        self.layout().addWidget(self.buttonbox, 0, 0, 2, 1)
        self.layout().addWidget(self.bar, 0, 0, 1, 1)

    def run(self):
        self.bar.pushMessage("Hello", "World", level=QgsMessageBar.INFO)


my_dialog = MyDialog()
my_dialog.show()


# Progress bar
progressMessageBar = iface.messageBar().createMessage("Doing something boring...")
progress = QProgressBar()
progress.setMaximum(10)
progress.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
progressMessageBar.layout().addWidget(progress)
iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)
for i in range(10):
    time.sleep(1)
    progress.setValue(i + 1)
iface.messageBar().clearWidgets()

msgBar = iface.messageBar()

pb = QProgressBar(msgBar)
msgBar.pushWidget(pb, QgsMessageBar.INFO, 5)

msg = msgBar.createMessage(u'Hello World')
msgBar.pushWidget(msg, QgsMessageBar.WARNING, 5)
