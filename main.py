'''base game functions'''
import pygame as pg
import sys
import constants as c
from player import Player
from sprites import Menus, ItemSprites
from Inventory import Inventory

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.clock = pg.time.Clock()
        self.gameStateManager = GameStateManager('level')

        # different game states
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)
        # dict of states
        self.states = {
            'start': self.start,
            'level': self.level
        }

    def set_screen(self):
        pg.display.set_caption("Scratch's Inventory")
        scratch_icon = pg.image.load(c.SPRITES['icon']).convert_alpha()
        pg.display.set_icon(scratch_icon)

    def main_game_loop(self):
        while True:

            #+==============+#
            #~~Event~Poller~~#
            #+==============+#
            keys = pg.key.get_pressed()
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

            self.states[self.gameStateManager.get_state()].run(events, keys)

            #+========+#
            #~~Screen~~#
            #+========+#

            pg.display.flip()

            self.clock.tick(60)
class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.player = Player(self.display)
        self.gameStateManager = gameStateManager
        self.inventory = Inventory(self.display, c.SPRITES['items'])
        self.sprites = ItemSprites(self.display, c.SPRITES['items'])

    def run(self, events, keys):
        self.display.fill('black')
        self.player.move(keys)
        self.player.draw(self.display, 'green')
        self.inventory.update(events)
        self.sprites.item_sprites()

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.start_menu = Menus(self.display, c.SPRITES['startMenu'])

    def run(self, events, keys):
        self.display.fill('gray4')
        self.start_menu.start_menu_sprites()
        self.start_menu.menu_options(events, self.gameStateManager)
        
            


class GameStateManager():
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.set_screen()
    game.main_game_loop()
