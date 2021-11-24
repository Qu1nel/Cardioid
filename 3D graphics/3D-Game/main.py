import sys
from math import cos, sin

import pygame as pg

from Player import Player
from map import world_map
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

        pg.draw.circle(self.screen, GREEN, self.player.pos, 13)
        pg.draw.line(self.screen, GREEN, self.player.pos,
                     (self.player.x + self.width * cos(self.player.angle),
                      self.player.y + self.width * sin(self.player.angle)))

        for x, y in world_map:
            pg.draw.rect(self.screen, DARKGRAY, (x, y, TILE, TILE), 2)

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
