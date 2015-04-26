class StatPanelRenderer:
    def __init__(self, player):
        """
        :param player: The game player.
        :type player: engine.player.Player
        """
        self.player = player

    def show_hp(self, window):
        """
        :param window: The window to draw to.
        """
        hpstr = "HP: {0}".format(self.player.hp)
        window.drawStr(2, 2, hpstr)

    def render(self, console):
        """
        :param console: A renderer.
        :type console: rendering.tdlrenderer.TdlRenderer
        """
        width, height = console.get_size()

        win = console.get_window(12, height)

        win.drawFrame(0, 0, 12, height, '-')

        self.show_hp(win)

        console.draw_window_at(width - 12, 0, win)
