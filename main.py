'''main game loop'''
import pygame as pg

import constants as c
from player import Player

pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Scratch's Inventory")
scratch_icon = pg.image.load(c.SPRITES['icon']).convert_alpha()
pg.display.set_icon(scratch_icon)
clock = pg.time.Clock()
player = Player()

running = True
while running:

    #+==============+#
    #~~Event~Poller~~#
    #+==============+#

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys == keys[pg.K_ESCAPE]:
        running = False

    player.move(keys)

    #+========+#
    #~~Screen~~#
    #+========+#

    screen.fill("black")

    #+=============+#
    #~~Render~Game~~#
    #+=============+#

    player.draw(screen, "red")


    pg.display.flip()

    clock.tick(60)

pg.quit()

    
