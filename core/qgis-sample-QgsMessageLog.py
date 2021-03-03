# coding: utf-8
from qgis.core import Qgis, QgsApplication


def writelogmessage(message, tag, level):
    with open(filename, 'a') as logfile:
        logfile.write('{}({}): {}'.format(tag, level, message))

filename = '/tmp/qgis.log'

message_log = QgsApplication.messageLog()
message_log.messageReceived.connect(writelogmessage)

# Use the QgsMessageLog to log all the information that you want to save
# about the execution of your code.
message_log.logMessage("Your plugin code has been executed correctly",
                         'MyPlugin', Qgis.Info)
message_log.logMessage("Your plugin code might have some problems",
                         level=Qgis.Warning)
message_log.logMessage("Your plugin code has crashed!",
                         level=Qgis.Critical)
