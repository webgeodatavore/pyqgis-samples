for widget in iface.mainWindow().children():
    if widget.objectName() == 'MessageLog':
        widget.show()

iface.mainWindow().findChild(QDockWidget, 'MessageLog').show()

iface.openMessageLog()

iface.mainWindow().findChild(QDockWidget, 'MessageLog').children()[4].objectName()

iface.mainWindow().findChild(QDockWidget, 'MessageLog').children()[4].hide()