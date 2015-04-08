class TdlRenderer:
    def __init__(self, width = 80, height = 24, title = 'TDL Console'):
        import tdl # Importhing this initializes a bunch of crap
        self.tdl = tdl # We don't want to import it a bunch of times though
        self.console = tdl.init(width, height, title)

    def draw_str_at(self, x, y, string, 
                    fgcolor = (255, 255, 255), bgcolor = (0, 0, 0)):
        self.console.drawStr(x, y, string, fgcolor = fgcolor, bgcolor = bgcolor)

    def pre_render(self):
        self.console.clear()

    def post_render(self):
        self.tdl.flush()

    def get_size(self):
        return self.console.getSize()

    def set_color(self, x, y, fg = None, bg = None):
        self.console.drawChar(x, y, None, fgcolor = fg, bgcolor = bg)
