from environment.npcs.monster import Monster
from environment.npcs.monstercontroller import MonsterController

class EnvironmentController:
    def __init__(self, map_info, player):
        self.map = map_info
        self.monsters = []
        self.player = player

    def validate_move(self, x, y):
        spaceinfo = self.map.get_attrs(x, y)
        if 'passable' in spaceinfo and spaceinfo['passable'] == False:
            return False
        if any(m.monster.get_location() == (x, y) for m in self.monsters):
            return False
        if self.player.get_location() == (x, y):
            return False
        return True

    def add_monster(self, monster = Monster(5, 5, 'kobold')):
        mc = MonsterController(monster)
        self.monsters.append(mc)
        return mc

    def update(self):
        for mc in self.monsters:
            mc.update(self)

    def render_monsters(self, renderer):
        for mc in self.monsters:
            renderer.render_monster(mc.monster)

    def entity_at(self, x, y):
        return next((m.monster for m in self.monsters if m.monster.get_location() == (x, y)), None)

    def remove_monster(self, monster):
        self.monsters.remove(monster)
