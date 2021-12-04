import sys
import config
import pygame as pg


class App(object):
    def __init__(self):
        self.width, self.height = (config.WIDTH, config.HEIGHT)
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

    def draw(self) -> None:
        self.screen.fill('black')
        pg.display.update()

    def run(self) -> None:
        while True:
            self.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.clock.tick(75)


if __name__ == '__main__':
    App().run()
