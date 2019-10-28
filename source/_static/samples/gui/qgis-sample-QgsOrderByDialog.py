# coding: utf-8
from qgis.gui import QgsOrderByDialog
from qgis.utils import iface

layer = iface.activeLayer()

order_by_dialog = QgsOrderByDialog(layer)

order_by = layer.rendererV2().orderBy()
clauses = order_by.list()  # List of OrderByClause

for clause in clauses:
    print('Expression: ' + clause.expression().expression())  # QgsExpression
    print('Ascending?: ' + str(clause.ascending()))  # Change value with setAscending
    print('nulls first? ' + str(clause.nullsFirst()))  # Change value with setNullsFirst
    print('Dump: ' + clause.dump())

order_by_dialog.setOrderBy(order_by)

order_by_dialog.show()
