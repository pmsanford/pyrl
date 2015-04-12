class PlayerController:
    movement_keys = ['up', 'down', 'left', 'right', 'ul', 'ur', 'dl', 'dr']
    def __init__(self, player, keybindings, game):
        self.player = player
        self.keybindings = keybindings
        self.game = game

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

        if command == 'up':
            self.player.set_location(x, y - 1)
        if command == 'down':
            self.player.set_location(x, y + 1)
        if command == 'left':
            self.player.set_location(x - 1, y)
        if command == 'right':
            self.player.set_location(x + 1, y)
        if command == 'ul':
            self.player.set_location(x - 1, y - 1)
        if command == 'ur':
            self.player.set_location(x + 1, y - 1)
        if command == 'dl':
            self.player.set_location(x - 1, y + 1)
        if command == 'dr':
            self.player.set_location(x + 1, y + 1)
