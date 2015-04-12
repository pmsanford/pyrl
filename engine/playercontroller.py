class PlayerController:
    movement_keys = ['up', 'down', 'left', 'right', 'ul', 'ur', 'dl', 'dr']
    def __init__(self, player, keybindings, game, environment):
        self.player = player
        self.keybindings = keybindings
        self.game = game
        self.env = environment

    def handle_keypress(self, event):
        command = self.keybindings.get_binding(event.keychar)
        if command is not None:
            if command in self.movement_keys:
                self.handle_movement(command)
            if command == 'attack':
                self.game.get_target()
    
    def resolve_attack(self, monster):
        if monster is not None:
            monster.hp -= 10

    def handle_movement(self, command):
        x, y = self.player.get_location()
        new_x = x
        new_y = y

        if command == 'up':
            new_y -= 1
        if command == 'down':
            new_y += 1
        if command == 'left':
            new_x -= 1
        if command == 'right':
            new_x += 1
        if command == 'ul':
            new_y -= 1
            new_x -= 1
        if command == 'ur':
            new_y -= 1
            new_x += 1
        if command == 'dl':
            new_y += 1
            new_x -= 1
        if command == 'dr':
            new_y += 1
            new_x += 1

        if self.env.validate_move(new_x, new_y):
            self.player.set_location(new_x, new_y)
