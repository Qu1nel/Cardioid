import sys

import pygame as pg


class App(object):
    def __init__(self):
        self.width, self.height = (1600, 900)
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

    def draw(self):
        self.screen.fill('black')
        pg.display.update()

    def run(self):
        while True:
            self.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.clock.tick(60)


if __name__ == '__main__':
    App().run()
