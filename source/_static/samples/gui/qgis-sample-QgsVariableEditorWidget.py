# coding: utf-8
from qgis.core import QgsExpressionContextUtils, QgsExpressionContext
from qgis.gui import QgsVariableEditorWidget
from qgis.utils import iface

canvas = iface.mapCanvas()
variable_editor_widget = QgsVariableEditorWidget()
expression_context = QgsExpressionContext()
expression_context.appendScope(QgsExpressionContextUtils.globalScope())
expression_context.appendScope(QgsExpressionContextUtils.projectScope())
expression_context.appendScope(QgsExpressionContextUtils.mapSettingsScope(
    canvas.mapSettings()
))
variable_editor_widget.setContext(expression_context)

variable_editor_widget.reloadContext()
variable_editor_widget.setEditableScopeIndex(0)
print(variable_editor_widget.context())
print(variable_editor_widget.editableScope())
print(variable_editor_widget.settingGroup())
print(variable_editor_widget.variablesInActiveScope())

variable_editor_widget.show()
