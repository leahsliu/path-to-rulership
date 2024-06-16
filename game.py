import pygame as pg
import sys
from scripts.utils import load_image
from scripts.entities import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Path to Rulership')

        self.screen = pg.display.set_mode((640, 480))
        self.display = pg.Surface((320, 240))

        self.clock = pg.time.Clock()

        self.movement = [False, False, False, False] # left, right, up, down


        self.assets = {
            'player-d1': load_image('player/down1.png'),
            'player-d2': load_image('player/down2.png'),
            'player-id1': load_image('player/idle1.png'),
            'player-id2': load_image('player/idle2.png'),
            'player-l1': load_image('player/left1.png'),
            'player-l2': load_image('player/left2.png'),
            'player-r1': load_image('player/right1.png'),
            'player-r2': load_image('player/right2.png'),
            'player-up1': load_image('player/up1.png'),
            'player-up2': load_image('player/up2.png')
        }

        self.player = Entities(self, 'player-d1', (10,10), (8,10))
    
    def run(self):
        while True:
             self.display.fill([255, 0, 0])
             self.player.update((self.movement[1]-self.movement[0], self.movement[3]-self.movement[2]))
             self.player.render(self.display)

             for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()   

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pg.K_UP:
                        self.movement[2] = True
                    if event.key == pg.K_DOWN:
                        self.movement[3] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pg.K_UP:
                        self.movement[2] = False
                    if event.key == pg.K_DOWN:
                        self.movement[3] = False
                self.screen.blit(self.display, (0,0))
                pg.display.update()
                self.clock.tick(60)

game = Game()
game.run()