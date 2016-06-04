# coding: utf-8
from PyQt4.QtGui import QFont
from qgis.gui import CharacterWidget

character_widget = CharacterWidget()


def on_selected_character(character):
    print(character)

character_widget.characterSelected.connect(on_selected_character)
character_widget.show()

print(character_widget.setCharacter('Z'))
print(character_widget.sizeHint())

print(character_widget.getColumns())
print(character_widget.updateColumns(6))

print(character_widget.getSquareSize())
print(character_widget.updateFont(QFont('Verdana')))
print(character_widget.updateSize(32))
print(character_widget.updateStyle('Bold'))
