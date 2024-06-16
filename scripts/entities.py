import pygame as pg


class Entities:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        # self.velocity = [0,0]


    def update(self, movement=(0,0)):
        # dx, dy = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        dx, dy = movement
        self.pos[0] += dx
        self.pos[1] += dy

    def render(self, display):
        display.blit(self.game.assets['player-d1'], self.pos)
