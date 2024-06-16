import pygame as pg

BASE_PATH = 'assets/'

def load_image(path):
    img = pg.image.load(BASE_PATH + path).convert()
    img.set_colorkey((0,0,0))

    return img