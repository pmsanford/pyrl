from rendering.tdlrenderwindow import TdlRenderWindow

class TdlRenderer:
    def __init__(self, width = 80, height = 24, title = 'TDL Console'):
        import tdl # Importhing this initializes a bunch of crap
        self.tdl = tdl # We don't want to import it a bunch of times though
        self.console = tdl.init(width, height, title)
        self.prompt = None

    def draw_str_at(self, x, y, string, 
                    fg = (255, 255, 255), bg = (0, 0, 0)):
        self.console.drawStr(x, y, string, fg = fg, bg = bg)

    def pre_render(self):
        self.console.clear()

    def post_render(self):
        if self.prompt is not None:
            self.console.blit(self.prompt, 0, self.console.height - 4)
        self.tdl.flush()

    def get_size(self):
        return self.console.getSize()

    def set_color(self, x, y, fg = None, bg = None):
        self.console.drawChar(x, y, None, fg = fg, bg = bg)
        
    def get_window(self, width, height):
        """
        Get a window to draw into.

        :param int width: Width of the window.
        :param int height: Height of the window.

        :return: Drawable window.
        """
        cons = self.tdl.Console(width, height)
        return TdlRenderWindow(width, height, cons)

    def draw_window_at(self, x, y, win):
        """
        Draw a console window to the screen.

        :param int x: X coordinate.
        :param int y: Y coordinate.
        """
        self.console.blit(win.win, x, y)

    def show_prompt(self, text):
        new_win = self.tdl.Console(self.console.width, 4)
        new_win.clear()
        new_win.drawFrame(0, 0, None, None, '-')
        new_win.drawStr(1, 1, text)
        new_win.move(1, 2)
        self.console.blit(new_win, 0, self.console.height - 4)
        self.prompt = new_win

    def clear_prompt(self):
        self.prompt = None
