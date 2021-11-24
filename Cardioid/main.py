import math
import sys

import pygame as pg


class Cardioid(object):
    def __init__(self, app):
        self.app = app
        self.radius = 350
        self.num_lines = 150
        self.translate = (self.app.screen.get_width() // 2, self.app.screen.get_height() // 2)
        self.counter, self.inc = (0, 0.01)

    def get_color(self) -> pg.Color:
        self.counter += self.inc
        if 0 < self.counter < 1:
            self.counter, self.inc = (self.counter, self.inc)
        else:
            self.counter, self.inc = (max(min(self.counter, 1), 0), -self.inc)

        return pg.Color('red').lerp('green', self.counter)

    def draw(self) -> None:
        time = pg.time.get_ticks()
        self.radius = abs(math.sin(time * 0.008) - 0.5) * 15 + 350
        factor = 1 + 0.00025 * time

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x1 = -int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            x2 = -int(self.radius * math.cos(theta * factor)) + self.translate[0]
            y2 = int(self.radius * math.sin(theta * factor)) + self.translate[1]

            pg.draw.aaline(self.app.screen, 'yellow', (x1, y1), (x2, y2))  # 'yellow' = self.get_color()


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
