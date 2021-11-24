import sys
from math import cos, sin

import pygame as pg

from Player import Player
from map import world_map
from ray_casting import ray_casting
from settings import *


class App(object):
    __slots__ = ('width', 'height', 'screen', 'clock', 'player')

    def __init__(self):
        self.width, self.height = (WIDTH, HEIGHT)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.player = Player()

    def draw(self) -> None:
        self.screen.fill(BLACK)

        # w

        ray_casting(self.screen, self.player.pos, self.player.angle)

        pg.display.update()

    def run(self) -> None:
        while True:
            self.player.movement()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    App().run()
