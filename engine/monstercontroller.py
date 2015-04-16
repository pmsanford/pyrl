class MonsterController:
    def __init__(self, monster, environment):
        self.monster = monster
        self.env = environment

    def update(self, environment):
        if self.monster.get_hp() <= 0:
            self.env.remove_monster(self)
