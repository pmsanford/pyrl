from environment.npcs.monster import Monster
from environment.npcs.monstercontroller import MonsterController

class EnvironmentController:
    def __init__(self, map_info, player):
        """
        Create new environment controller.

        :param map_info: Map description.
        :type map_info: environment.map.Map
        :param player: Player object
        :type player: engine.player.Player
        """
        self.map = map_info
        self.monsters = []
        self.player = player

    def validate_move(self, x, y):
        """
        Find out if moving into a given space is valid.

        :param int x: x coordinate
        :param int y: y coordinate

        :return: Whether it is valid to move into location.
        :rtype: bool
        """
        spaceinfo = self.map.get_attrs(x, y)
        if 'passable' in spaceinfo and spaceinfo['passable'] == False:
            return False
        if any(m.monster.get_location() == (x, y) for m in self.monsters):
            return False
        if self.player.get_location() == (x, y):
            return False
        return True

    def add_monster(self, monster = Monster(5, 5, 'kobold')):
        """
        Add a monster to the environment.

        :param monster: The monster to add.
        :type monster: environment.npcs.monster.Monster
        """
        mc = MonsterController(monster)
        self.monsters.append(mc)
        return mc

    def update(self):
        """
        Update all monsters in the environment.
        """
        for mc in self.monsters:
            mc.update(self)

    def render_monsters(self, renderer):
        """
        Render all monsters to the screen.
        """
        for mc in self.monsters:
            renderer.render_monster(mc.monster)

    def entity_at(self, x, y):
        """
        Returns the entity at the given location, or none if there are none.

        :param int x: x coord.
        :param int y: y coord.

        :return: Entity at location, or none.
        """
        return next((m.monster for m in self.monsters if m.monster.get_location() == (x, y)), None)

    def remove_monster(self, monster):
        """
        Remove given monster.

        :param Monster monster: The monster to remove.
        """
        self.monsters.remove(monster)

    def get_player_pos(self):
        """
        Get player position.

        :return: Player's position (x, y)
        :rtype: tuple
        """
        return self.player.position
