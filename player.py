'''Player Class'''
import pygame as pg

class Player():
    def __init__(self):
        self.rect = pg.Rect(380, 380, 32, 32)
        self.speed = 4

    def draw(self, screen, color):
        '''draw character on screen'''
        pg.draw.rect(screen, color, self.rect)

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