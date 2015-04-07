import tdl
from environment.map import Map
from rendering.tdlrenderer import TdlRenderer
from graphics.texttileset import TextTileset
from rendering.textmaprenderer import TextMapRenderer
from rendering.characterrenderer import CharacterRenderer
from engine.player import Player

WIDTH, HEIGHT = 80, 24

MOVEMENT_KEYS = {
        'UP': [0, -1],
        'DOWN': [0, 1],
        'LEFT': [-1, 0],
        'RIGHT': [1, 0],

        'K': [0, -1],
        'J': [0, 1],
        'H': [-1, 0],
        'L': [1, 0],
        'Y': [-1, -1],
        'B': [-1, 1],
        'U': [1, -1],
        'N': [1, 1],
        }

console = TdlRenderer(WIDTH, HEIGHT, 'sandbox')

cur_map = Map()

map_tileset = TextTileset('text_tiles.json')
char_tileset = TextTileset('char_tiles.json')

map_renderer = TextMapRenderer(console, map_tileset)
char_renderer = CharacterRenderer(console, char_tileset)

player = Player(1, 1, 'player')

while True:
    console.clear()

    map_renderer.render_map(cur_map)
    
    char_renderer.render_character(player)

    playerX, playerY = player.get_location()

    visible = tdl.map.quickFOV(playerX, playerY, cur_map.is_passable, radius=20)

    for posX, posY in visible:
        console.set_color(posX, posY, fg = (255, 255, 0))

    console.flush()

    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
            if event.keychar.upper() in MOVEMENT_KEYS:
                keyX, keyY = MOVEMENT_KEYS[event.keychar.upper()]

                newX = playerX + keyX
                newY = playerY + keyY

                if cur_map.is_passable(newX, newY):
                    player.set_location(newX, newY)
            
            if event.keychar.upper() == 'Q':
                raise SystemExit('Bye felicia')

        if event.type == 'QUIT':
            raise SystemExit('Bye felicia')
