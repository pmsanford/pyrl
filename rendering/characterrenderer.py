class CharacterRenderer:
    def __init__(self, console, tileset):
        self.tileset = tileset
        self.console = console

    def render_character(self, character):
        tile = self.tileset.get_tile(character.tile_code)

        self.console.draw_str_at(character.x, character.y, 
                                tile['char'], tile['color'])
