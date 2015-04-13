class Monster:
    def __init__(self, x, y, tile_code, hp = 100):
        self.tile_code = tile_code
        self.x = x
        self.y = y
        self.hp = hp

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return (self.x, self.y)

    def take_damage(self, amount):
        self.hp -= amount

    def get_hp(self):
        return self.hp
