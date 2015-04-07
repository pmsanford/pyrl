import tdl
from map import Map
from rendering.tdlrenderer import TdlRenderer

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

playerX, playerY = 1, 2

while True:
    console.clear()

    cur_map = Map()

    cur_map.draw(console)

    console.draw_str_at(playerX, playerY, '@')

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
                    playerX = newX
                    playerY = newY
            
            if event.keychar.upper() == 'Q':
                raise SystemExit('Bye felicia')

        if event.type == 'QUIT':
            raise SystemExit('Bye felicia')
