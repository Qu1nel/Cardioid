import sys

import pygame as pg

from Player import Player
from settings import *


class App(object):
    def __init__(self):
        self.width, self.height = (WIDTH, HEIGHT)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.player = Player()

    def draw(self) -> None:
        self.screen.fill(BLACK)
        pg.draw.circle(self.screen, GREEN, self.player.pos, 13)
        pg.display.update()

    def run(self) -> None:
        while True:
            self.draw()
            self.player.movement()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.clock.tick(120)


if __name__ == '__main__':
    App().run()
