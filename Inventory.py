'''class for inventory'''
import pygame as pg
from items import *
from sprites import ItemSprites

class Inventory():
    def __init__(self, screen, image) -> None:
        self.screen = screen
        self.item_sprite = ItemSprites(screen, image)
        
        self.slots = []
        for index in range(5):
            self.slots.append(Item())
        self.slots[1] = WeponItem('sword', 2)
        self.slots[2] = WeponItem('mace', 3)

        self.active_slot = 0

    def debug(self):
        for slot in self.slots:
            print(slot)

    # def use(self, player, position):
    #     if self.slots[self.active_slot].name != 'item':
    #         self.slots[self.active_slot].use(player)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHTBRACKET:
                    if self.active_slot < len(self.slots)-1:
                        self.active_slot += 1
                if event.key == pg.K_LEFTBRACKET:
                    if self.active_slot > 0:
                        self.active_slot -= 1
                if event.key == pg.K_i:
                    self.debug()

    # def draw_items(self):
    #     items = self.item_sprite.item_sprites()