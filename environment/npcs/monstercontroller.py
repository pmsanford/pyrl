class MonsterController:
    def __init__(self, monster, environment):
        self.monster = monster
        self.env = environment
        self.behaviors = []

    def update(self, environment):
        if self.monster.get_hp() <= 0:
            self.env.remove_monster(self)
        for behavior in self.behaviors:
            if behavior.behave(self.monster, self.env):
                break

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)
