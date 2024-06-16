import pygame as pg


class Entities:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]


    def update(self, movement=(0,0)):
        dx, dy = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        # dx, dy = movement
        self.pos[0] += dx
        self.pos[1] += dy

        # Boundary check to keep entity within screen
        self.pos[0] = max(0, min(self.pos[0], self.game.display.get_width() - self.size[0]))
        self.pos[1] = max(0, min(self.pos[1], self.game.display.get_height() - self.size[1]))
        print(f"Player position: {self.pos}, Velocity: {self.velocity}")  # Debugging line


    def render(self, display):
        display.blit(self.game.assets[self.type], self.pos)
