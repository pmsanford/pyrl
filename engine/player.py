class Player:
    def __init__(self, x, y, tile_code):
        self.tile_code = tile_code
        self.x = x
        self.y = y

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return (self.x, self.y)
