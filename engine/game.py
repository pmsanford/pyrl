import config
from environment.map import Map
from rendering.tdlrenderer import TdlRenderer
from graphics.texttileset import TextTileset
from rendering.textmaprenderer import TextMapRenderer
from rendering.characterrenderer import CharacterRenderer
from engine.player import Player
from input.tdlinput import TdlInput
from input.keybindings import Keybindings
from engine.playercontroller import PlayerController

class Game:
    def __init__(self, console = TdlRenderer(config.WIDTH, config.HEIGHT, 'Game'),
                 first_map = Map(),
                 map_tileset = TextTileset(config.get_game_data('text_tiles.json')),
                 char_tileset = TextTileset(config.get_game_data('char_tiles.json')),
                 map_renderer = None,
                 char_renderer = None,
                 player = Player(1, 1, 'player'),
                 input_processor = TdlInput(),
                 keybindings = Keybindings(config.get_game_data('keybindings.json')),
                 player_controller = None):
        self.console = console
        self.cur_map = first_map
        self.map_tileset = map_tileset
        self.char_tileset = char_tileset
        self.map_renderer = map_renderer if map_renderer is not None else TextMapRenderer(console, map_tileset)
        self.char_renderer = char_renderer if char_renderer is not None else CharacterRenderer(console, char_tileset)
        self.player = player
        self.input_processor = input_processor
        self.input_processor.add_event_handler(self.handle_quit, ['quit'])
        self.keybindings = keybindings
        self.player_controller = player_controller if player_controller is not None else PlayerController(player, keybindings, self)
        self.input_processor.add_event_handler(self.handle_keypress, ['key'])
        self.state = 'movement'

    def handle_keypress(self, event):
        if event.keychar.upper() == 'Q':
            raise SystemExit("User pressed q")
        if self.state == 'movement':
            self.player_controller.handle_keypress(event)
        elif self.state == 'attack':
            self.finish_attack(event.keychar)

    def finish_attack(self, keypress):
        self.player_controller.resolve_attack(None)
        self.console.clear_prompt()
        self.state = 'movement'

    def get_target(self):
        self.state = 'attack'
        self.console.show_prompt("Which direction?")
        self.console.post_render()

    def handle_quit(self, event):
        raise SystemExit("User closed window")

    def render_all(self):
        self.console.pre_render()
        self.map_renderer.render_map(self.cur_map)
        self.char_renderer.render_character(self.player)
        self.console.post_render()

    def handle_events(self):
        self.input_processor.poll_events()

    def loop(self):
        while True:
            self.render_all()
            self.handle_events()
