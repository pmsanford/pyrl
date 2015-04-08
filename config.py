from os.path import join, abspath
from os import getcwd
WIDTH = 80
HEIGHT = 24

DATA_PATH = 'gamedata'

def get_game_data(filename):
    return abspath(join(DATA_PATH, filename))
