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
from environment.environmentcontroller import EnvironmentController
from rendering.monsterrenderer import MonsterRenderer
from environment.npcs.behaviors.randommove import RandomMove

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
                 player_controller = None,
                 environment = None):
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
        self.environment = environment if environment is not None else EnvironmentController(self.cur_map, self.player)
        self.player_controller = player_controller if player_controller is not None else PlayerController(player, keybindings, self, self.environment)
        self.input_processor.add_event_handler(self.handle_keypress, ['key'])
        self.state = 'movement'
        mc = self.environment.add_monster()
        mc.add_behavior(RandomMove())

    def handle_keypress(self, event):
        if event.keychar.upper() == 'Q':
            raise SystemExit("User pressed q")
        if self.state == 'movement':
            self.player_controller.handle_keypress(event)
        elif self.state == 'attack':
            self.finish_attack(event.keychar)

    def get_loc_from_dir(self, cmd):
        x, y = self.player.get_location()
        new_x = x
        new_y = y

        if cmd == 'up':
            new_y -= 1
        if cmd == 'down':
            new_y += 1
        if cmd == 'left':
            new_x -= 1
        if cmd == 'right':
            new_x += 1
        if cmd == 'ul':
            new_y -= 1
            new_x -= 1
        if cmd == 'ur':
            new_y -= 1
            new_x += 1
        if cmd == 'dl':
            new_y += 1
            new_x -= 1
        if cmd == 'dr':
            new_y += 1
            new_x += 1

        return (new_x, new_y)

    def finish_attack(self, keypress):
        cmd = self.keybindings.get_binding(keypress)
        x, y = self.get_loc_from_dir(cmd)
        monst = self.environment.entity_at(x, y)
        self.player_controller.resolve_attack(monst)
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
        self.environment.render_monsters(
                MonsterRenderer(self.console, self.char_tileset))
        self.console.post_render()

    def update_all(self):
        self.environment.update()

    def turn_completed(self):
        self.update_all()

    def handle_events(self):
        self.input_processor.poll_events()

    def loop(self):
        while True:
            self.render_all()
            self.handle_events()
