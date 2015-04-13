class MonsterController:
    def __init__(self, monster, game):
        self.monster = monster
        self.game = game

    def update(self):
        if self.monster.get_hp() <= 0:
            self.game.remove(self)
