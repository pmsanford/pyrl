class TdlRenderer:
    def __init__(self, width = 80, height = 24, title = 'TDL Console'):
        import tdl # Importhing this initializes a bunch of crap
        self.tdl = tdl # We don't want to import it a bunch of times though
        self.console = tdl.init(width, height, title)
        self.prompt = None

    def draw_str_at(self, x, y, string, 
                    fgcolor = (255, 255, 255), bgcolor = (0, 0, 0)):
        self.console.drawStr(x, y, string, fgcolor = fgcolor, bgcolor = bgcolor)

    def pre_render(self):
        self.console.clear()

    def post_render(self):
        if self.prompt is not None:
            self.show_prompt(self.prompt)
        self.tdl.flush()

    def get_size(self):
        return self.console.getSize()

    def set_color(self, x, y, fg = None, bg = None):
        self.console.drawChar(x, y, None, fgcolor = fg, bgcolor = bg)

    def show_prompt(self, text):
        new_win = self.tdl.Window(self.console, 0, self.console.height - 4, self.console.width, 4)
        new_win.clear()
        new_win.drawFrame(0, 0, self.console.width, 4, '-')
        new_win.drawStr(1, 1, text)
        new_win.move(1, 2)
        self.console.blit(new_win, 0, self.console.height - 4)
        self.prompt = text

    def clear_prompt(self):
        self.prompt = None
