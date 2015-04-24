class ChasePlayer:
    def behave(self, monster, environment):
        """
        Move toward the player.

        :param monster: Monster to behave.
        :type monster: environment.npcs.monster.Monster
        :param environment: Evironment in which the monster resides.
        :type environment: environment.environmentcontroller.EnvironmentController
        
        :returns: Whether the monster took this action.
        :rtype: bool
        """
        import tdl

        seek_x, seek_y = environment.get_player_pos()

        dim_x, dim_y = environment.map.get_dimensions()

        from_x, from_y = monster.get_location()

        path = tdl.map.AStar(dim_x, dim_y, environment.get_move_cost, advanced=True)

        series = path.getPath(from_x, from_y, seek_x, seek_y)

        if len(series) > 1:
            monster.set_location(series[0][0], series[0][1])
            return True
        else:
            return False
