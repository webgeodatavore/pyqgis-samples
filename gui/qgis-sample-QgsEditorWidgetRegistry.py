# coding: utf-8
from qgis.gui import QgsEditorWidgetRegistry

editor_widget_registry_instance = QgsEditorWidgetRegistry.instance()

# List available widgets in Text edition in tab Fields of a vector layer
print editor_widget_registry_instance.factories()  # Return a list of QgsEditorWidgetFactory
print editor_widget_registry_instance.factories().keys()

# Get QgsEditorWidgetFactory
print editor_widget_registry_instance.factory(u'Range')
print editor_widget_registry_instance.factory(u'RelationReference')

"""
Classes below inherit from QgsEditorWidgetFactory and are the one really used.
They are casted

QgsCheckboxWidgetFactory
QgsClassificationWidgetWrapperFactory
QgsColorWidgetFactory
QgsDateTimeEditFactory
QgsEnumerationWidgetFactory
QgsFileNameWidgetFactory
QgsHiddenWidgetFactory
QgsPhotoWidgetFactory
QgsRangeWidgetFactory
QgsRelationReferenceFactory
QgsTextEditWidgetFactory
QgsUniqueValueWidgetFactory
QgsUuidWidgetFactory
QgsValueMapWidgetFactory
QgsValueRelationWidgetFactory
QgsWebViewWidgetFactory
"""
