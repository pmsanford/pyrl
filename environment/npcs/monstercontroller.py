class MonsterController:
    def __init__(self, monster):
        """
        :param monster: The monster controlled by this controller.
        :type monster: environment.npcs.monster.Monster
        """
        self.monster = monster
        self.behaviors = []

    def update(self, environment):
        """
        :param environment: The environment in which the monster resides.
        :type environment: environment.environmentcontroller.EnvironmentController
        """
        if self.monster.get_hp() <= 0:
            environment.remove_monster(self)
        for behavior in self.behaviors:
            if behavior.behave(self.monster, environment):
                break

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)
