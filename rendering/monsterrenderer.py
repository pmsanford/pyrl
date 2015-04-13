class MonsterRenderer:
    def __init__(self, console, tileset):
        self.tileset = tileset
        self.console = console

    def render_monster(self, monster):
        tile = self.tileset.get_tile(monster.tile_code)

        self.console.draw_str_at(monster.x, monster.y, 
                                tile['char'], tile['color'])
