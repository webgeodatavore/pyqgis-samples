# coding: utf-8
import os
import random
from inspect import getsourcefile
from PyQt4 import uic
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QColorDialog, QVBoxLayout
from qgis.core import (QGis, QgsFeatureRendererV2,
                       QgsRendererV2AbstractMetadata, QgsRendererV2Registry,
                       QgsStyleV2, QgsSymbolV2)
from qgis.gui import QgsColorButtonV2, QgsRendererV2Widget
from qgis.utils import iface

directory = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))

WIDGET, BASE = uic.loadUiType(
    os.path.join(
        directory,
        '../ui/milstd2525rendererwidgetbase.ui'
    )
)


class RandomRenderer(QgsFeatureRendererV2):
    def __init__(self, syms=None):
        QgsFeatureRendererV2.__init__(self, "RandomRenderer")
        self.syms = syms if syms else [
            QgsSymbolV2.defaultSymbol(QGis.Point),
            QgsSymbolV2.defaultSymbol(QGis.Point)
        ]

    def symbolForFeature(self, feature):
        return random.choice(self.syms)

    def startRender(self, context, vlayer):
        for s in self.syms:
            s.startRender(context)

    def stopRender(self, context):
        for s in self.syms:
            s.stopRender(context)

    def usedAttributes(self):
        return []

    def clone(self):
        return RandomRenderer(self.syms)


class RandomRendererWidget(QgsRendererV2Widget, WIDGET):
    def __init__(self, layer, style, renderer):
        QgsRendererV2Widget.__init__(self, layer, style)
        self.setupUi(self)
        if renderer is None or renderer.type() != "RandomRenderer":
            self.r = RandomRenderer()
        else:
            self.r = renderer
        # setup UI
        self.btn1 = QgsColorButtonV2()
        self.btn1.setColor(self.r.syms[0].color())
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn1)
        self.setLayout(self.vbox)
        self.connect(self.btn1, SIGNAL("clicked()"), self.setColor1)

    def setColor1(self):
        color = QColorDialog.getColor(self.r.syms[0].color(), self)
        if not color.isValid():
            return
        self.r.syms[0].setColor(color)
        self.btn1.setColor(self.r.syms[0].color())

    def renderer(self):
        return self.r


class RandomRendererMetadata(QgsRendererV2AbstractMetadata):
    def __init__(self):
        QgsRendererV2AbstractMetadata.__init__(
            self,
            "RandomRenderer",
            "Random renderer"
        )

    def createRenderer(self, element):
        return RandomRenderer()

    def createRendererWidget(self, layer, style, renderer):
        return RandomRendererWidget(layer, style, renderer)

QgsRendererV2Registry.instance().addRenderer(RandomRendererMetadata())

print(QgsRendererV2Registry.instance().renderersList())
print(QgsRendererV2Registry.instance().rendererMetadata(u'RandomRenderer'))

layer, canvas = iface.activeLayer(), iface.mapCanvas()

style = QgsStyleV2.defaultStyle()
random_renderer_widget = RandomRendererWidget(
    layer,
    style,
    RandomRenderer()
)

# random_renderer_widget.show()

layer.setRendererV2(random_renderer_widget.r)

if iface.mapCanvas().isCachingEnabled():
    layer.setCacheImage(None)
else:
    canvas.refresh()
