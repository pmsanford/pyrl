class StatPanelRenderer:
    def __init__(self, player, console):
        """
        :param player: The game player.
        :type player: engine.player.Player
        """
        self.player = player
        self.console = console

    def show_hp(self, window):
        """
        :param window: The window to draw to.
        """
        hpstr = "HP: {0}".format(self.player.hp)
        window.drawStr(2, 2, hpstr)

    def render(self):
        """
        :param console: A renderer.
        :type console: rendering.tdlrenderer.TdlRenderer
        """
        width, height = self.console.get_size()

        win = self.console.get_window(12, height)

        win.drawFrame(0, 0, 12, height, '-')

        self.show_hp(win)

        self.console.draw_window_at(width - 12, 0, win)
