class TextMapRenderer:
    def __init__(self, console, tileset):
        self.console = console
        self.tileset = tileset

    def render_map(self, map_data):
        map_runs = map_data.get_runs()

        for run in map_runs:
            tile = self.tileset.get_tile(run.tile_code)
            run_text = tile['char'] * run.length
            self.console.draw_str_at(run.x, run.y, run_text, tile['color'])
