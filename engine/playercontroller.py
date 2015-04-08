class PlayerController:
    def __init__(self, player, keybindings):
        self.player = player
        self.keybindings = keybindings

    def handle_keypress(self, event):
        command = self.keybindings.get_binding(event.keychar)
        if command is not None:
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
