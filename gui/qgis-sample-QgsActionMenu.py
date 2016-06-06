# coding: utf-8
from qgis.gui import QgsActionMenu
from qgis.utils import iface

layer = iface.activeLayer()
if iface.activeLayer().actions().size() > 0:
    features = layer.dataProvider().getFeatures()
    feat1 = features.next()
    action_menu = QgsActionMenu(
        layer,
        feat1
    )
    print(feat1.id())

    action_menu.show()
    print(action_menu.actions())
    feat2 = features.next()
    action_menu.setFeature(feat2)
    print(feat2.id())
else:
    print('No action for this layer')
