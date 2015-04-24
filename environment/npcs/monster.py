class Monster:
    def __init__(self, x, y, tile_code, hp = 100):
        """
        Create a new monster

        :param int x: Initial location, x coord.
        :param int y: Initial location, y coord.
        :param str tile_code: Name of the tile to represent monster.
        :param int hp: Initial health.
        """
        self.tile_code = tile_code
        self.x = x
        self.y = y
        self.hp = hp

    def set_location(self, x, y):
        """
        Set the location of the monster.

        :param int x: New location, x coord.
        :param int y: New location, y coord.
        """
        self.x = x
        self.y = y

    def get_location(self):
        """
        Get the location of the monster.

        :return: Monster's location (x, y).
        :rtype: tuple
        """
        return (self.x, self.y)

    def take_damage(self, amount):
        """
        Deal damage to the monster.

        :param int amount: Amount of damage dealt.
        """
        self.hp -= amount

    def get_hp(self):
        """
        Get the monster's HP.

        :return: Monster's current HP.
        :rtype: int
        """
        return self.hp

    def get_damage_amount(self):
        """
        Get the amount of damage done by this monster's attack.

        :return: Damage amount.
        :rtype: int
        """
        return 5
