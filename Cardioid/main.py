import math
import sys

import pygame as pg


class Cardioid(object):
    def __init__(self, app):
        self.app = app
        self.radius = 400
        self.num_lines = 300
        self.translate = (self.app.screen.get_width() // 2, self.app.screen.get_height() // 2)

    def draw(self) -> None:
        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            x2 = int(self.radius * math.cos(theta * 2)) + self.translate[0]
            y2 = int(self.radius * math.sin(theta * 2)) + self.translate[1]

            pg.draw.aaline(self.app.screen, 'green', (x1, y1), (x2, y2))


class App(object):
    def __init__(self):
        self.width, self.height = (1600, 900)
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)

    def draw(self) -> None:
        self.screen.fill('black')
        self.cardioid.draw()
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
