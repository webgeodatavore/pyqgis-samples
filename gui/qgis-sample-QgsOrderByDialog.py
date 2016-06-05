# coding: utf-8
from qgis.gui import QgsOrderByDialog
from qgis.utils import iface


order_by_dialog = QgsOrderByDialog(iface.activeLayer())

order_by_dialog.show()

order_by = iface.activeLayer().rendererV2().orderBy()
clauses = order_by.list()  # List of OrderByClause

for clause in clauses:
    print('Expression: ' + clause.expression().expression())  # QgsExpression
    print('Ascending?: ' + str(clause.ascending()))  # Change value with setAscending
    print('nulls first? ' + str(clause.nullsFirst()))  # Change value with setNullsFirst
    print('Dump: ' + clause.dump())
