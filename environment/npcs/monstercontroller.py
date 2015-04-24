class MonsterController:
    def __init__(self, monster):
        """
        Create a new monster controller.

        :param monster: The monster controlled by this controller.
        :type monster: environment.npcs.monster.Monster
        """
        self.monster = monster
        self.behaviors = []

    def update(self, environment):
        """
        Performs all the actions the monster needs to every frame. This
        method iterates over the available behaviors. Once a behavior
        notifies the method that it has acted, the method returns.


        :param environment: The environment in which the monster resides.
        :type environment: environment.environmentcontroller.EnvironmentController
        """
        if self.monster.get_hp() <= 0:
            environment.remove_monster(self)
        for behavior in self.behaviors:
            if behavior.behave(self.monster, environment):
                break

    def add_behavior(self, behavior):
        """
        Add a behavior to the list of possible behaviors for the monster.

        :param behavior: The new behavior to add.
        """
        self.behaviors.append(behavior)
