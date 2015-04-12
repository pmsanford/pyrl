class EnvironmentController:
    def __init__(self, map_info):
        self.map = map_info

    def validate_move(self, x, y):
        spaceinfo = self.map.get_attrs(x, y)
        if 'passable' in spaceinfo and spaceinfo['passable'] == False:
            return False
        return True
