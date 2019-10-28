# coding: utf-8
from qgis.core import QgsMessageLog

filename = '/tmp/qgis.log'


def writelogmessage(message, tag, level):
    with open(filename, 'a') as logfile:
        logfile.write('{}({}): {}'.format(tag, level, message))

QgsMessageLog.instance().messageReceived.connect(writelogmessage)

# Use QgsMessageLog to log all the information that you want to save about
# the execution of your code.
QgsMessageLog.logMessage("Your plugin code has been executed correctly",
                         'MyPlugin', QgsMessageLog.INFO)
QgsMessageLog.logMessage("Your plugin code might have some problems",
                         level=QgsMessageLog.WARNING)
QgsMessageLog.logMessage("Your plugin code has crashed!",
                         level=QgsMessageLog.CRITICAL)
