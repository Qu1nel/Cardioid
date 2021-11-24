import sys

import pygame as pg

from settings import *





class App(object):
    def __init__(self):
        self.width, self.height = (WIDTH, HEIGHT)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def draw(self) -> None:
        self.screen.fill(BLACK)
        pg.draw.circle(self.screen, GREEN, Player().position, 13)
        pg.display.update()

    def run(self) -> None:
        while True:
            self.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.clock.tick(60)


if __name__ == '__main__':
    App().run()
