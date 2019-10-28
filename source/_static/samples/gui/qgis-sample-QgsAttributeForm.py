from qgis.gui import QgsAttributeForm
from qgis.utils import iface

layer = iface.activeLayer()
attribute_form = QgsAttributeForm(layer, next(layer.getFeatures()))
attribute_form.setMode(QgsAttributeForm.SingleEditMode.real) # SingleEditMode, AddFeatureMode, MultiEditMode, SearchMode, AggregateSearchMode, IdentifyMode

attribute_form.show()
