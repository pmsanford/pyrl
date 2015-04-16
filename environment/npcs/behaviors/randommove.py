import random

class RandomMove:
    def behave(self, monster, environment):
        x, y = monster.get_location()

        x_mov = random.randint(-1, 1)
        y_mov = random.randint(-1, 1)

        if environment.validate_move(x + x_mov, y + y_mov):
            monster.set_location(x + x_mov, y + y_mov)
            return True

        return False
