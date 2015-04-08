import config
from environment.map import Map
from rendering.tdlrenderer import TdlRenderer
from graphics.texttileset import TextTileset
from rendering.textmaprenderer import TextMapRenderer
from rendering.characterrenderer import CharacterRenderer
from engine.player import Player

class Game:
    def __init__(self, console = TdlRenderer(config.WIDTH, config.HEIGHT, 'Game'),
                 first_map = Map(),
                 map_tileset = TextTileset('text_tiles.json'),
                 char_tileset = TextTileset('char_tiles.json'),
                 map_renderer = None,
                 char_renderer = None,
                 player = Player(1, 1, 'player')):
        self.console = console
        self.cur_map = first_map
        self.map_tileset = map_tileset
        self.char_tileset = char_tileset
        self.map_renderer = map_renderer if map_renderer is not None else TextMapRenderer(console, map_tileset)
        self.char_renderer = char_renderer if char_renderer is not None else CharacterRenderer(console, char_tileset)
        self.player = player

    def render_all(self):
        self.console.clear()
        self.map_renderer.render_map(self.cur_map)
        self.char_renderer.render_character(self.player)
        self.console.flush()

    # TODO
    def handle_events(self):
        import tdl # TODO: Remove after refactoring handle_events
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                if event.keychar.upper() == 'Q':
                    raise SystemExit("User quit")

            if event.type == 'QUIT':
                raise SystemExit("User closed window")

    def loop(self):
        while True:
            self.render_all()
            self.handle_events()
