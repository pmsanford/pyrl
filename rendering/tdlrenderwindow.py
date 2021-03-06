class TdlRenderWindow:
    def __init__(self, width, height, win):
        """
        :param int width: Width of window.
        :param int height: Height of window.
        :param win: TDL Window.
        """
        self.width = width
        self.height = height
        self.win = win

    def draw_str_at(self, x, y, string, fg = (255, 255, 255),
                    bg = (0, 0, 0)):
        self.win.drawStr(x, y, string, fg = fg, bg = bg)

    def pre_render(self):
        self.win.clear()
    
    def post_render(self):
        pass

    def get_size(self):
        return self.win.getSize()

    def set_color(self, x, y, fg = None, bg = None):
        self.win.drawChar(x, y, None, fg = fg, bg = bg)

    def draw_frame(self, frame_char, x = 0, y = 0, width = None, height = None,
                    fg = (255, 255, 255), bg = (0, 0, 0)):
        width = width if width is not None else self.width
        height = height if height is not None else self.height
        self.win.drawFrame(x, y, width, height, frame_char)
