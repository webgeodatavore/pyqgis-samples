from qgis.PyQt.QtGui import QFont
from qgis.gui import CharacterWidget

character_widget = CharacterWidget()


def on_selected_character(character):
    print(character)

character_widget.characterSelected.connect(on_selected_character)
character_widget.show()

print(character_widget.setCharacter('Z'))
print(character_widget.sizeHint())

print(character_widget.columns())
print(character_widget.setColumns(6))

print(character_widget.squareSize())
print(character_widget.setFont(QFont('Verdana')))
print(character_widget.setFontSize(14))
print(character_widget.setFontStyle('Bold'))

# TODO: fix issue when resizing window that duplicates characters choices