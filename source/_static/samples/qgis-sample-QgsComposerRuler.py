# coding: utf-8
from qgis.core import QgsComposition
from qgis.gui import QgsComposerRuler
from qgis.utils import iface

composer_ruler = QgsComposerRuler(QgsComposerRuler.Vertical)
composition = QgsComposition(iface.mapCanvas().mapSettings())
composer_ruler.setComposition(composition)

composer_ruler.show()
