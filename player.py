'''Player Class'''
import pygame as pg
import constants as c
from sprites import Animation

class Player():
    def __init__(self, display):
        self.display = display
        self.rect = pg.Rect(0, 0, 94, 94)
        self.animation = Animation(self.display, c.SPRITES['scratch'])
        self.speed = 4

    def draw(self, screen, color):
        '''draw character on screen'''
        pg.draw.rect(screen, color, self.rect, 3)
        self.animation.player_animation(0, self.rect)

    def move(self, keys):
        '''move the player around the screen'''
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.move_ip(0, -self.speed)
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.move_ip(0, +self.speed)
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.move_ip(+self.speed, 0)
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.move_ip(-self.speed, 0)