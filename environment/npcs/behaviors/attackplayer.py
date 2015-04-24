class AttackPlayer:
    def behave(self, monster, environment):
        """
        Attempt to attack the player if you're next to him.

        :param monster: Monster to behave for.
        :type monster: environment.npcs.monster.Monster
        :param environment: Evironment in which the monster resides.
        :type environment: environment.environmentcontroller.EnvironmentController
        
        :returns: Whether the monster took this action.
        :rtype: bool
        """

        player_x, player_y = environment.get_player_pos()

        my_x, my_y = monster.get_location()

        if abs(player_x - my_x) <= 1 and abs(player_y - my_y) <= 1:
            environment.get_player().take_damage(monster.get_damage_amount())
            return True

        return False
