import json
import sys

class TextTileset:
    def __init__(self):
        tfile = open('text_tiles.json')
        tile_file = json.loads(tfile.read())
        tfile.close()
        self.tileset_name = tile_file['name']
        self.tiles = tile_file['tiles']

    def get_tile(self, tiledef):
        if tiledef in self.tiles:
            return self.tiles[tiledef]
        else:
            return None
