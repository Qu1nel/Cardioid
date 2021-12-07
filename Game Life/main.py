from sys import exit

import pygame as pg

import config as c


class GameLife(object):
    def __init__(self, app, sc: pg.Surface):
        self.app = app
        self.sc = sc
        self.color_cell = c.COLOR_CELL
        self.area = [[(x, y) for x in range(self.app.width // c.SIZE_CELL)] for y in
                     range(self.app.height // c.SIZE_CELL)]

    def draw_area(self):
        normalized = lambda coord: [i * c.SIZE_CELL for i in coord]
        for row in self.area:
            for cell in row:
                pg.draw.rect(surface=self.sc,
                             color=c.COLOR_CELL,
                             rect=pg.Rect(normalized(cell), (c.SIZE_CELL - 2, c.SIZE_CELL - 2)))


class App(object):
    def __init__(self):
        self.width, self.height = (c.WIDTH, c.HEIGHT)
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
        self.clock = pg.time.Clock()
        self.game_life = GameLife(self, self.screen)

    @staticmethod
    def handle_events() -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()

    def process(self) -> None:
        pass

    def draw(self) -> None:
        self.screen.fill(c.COLOR_BG)
        self.game_life.draw_area()
        pg.display.update()

    def run(self) -> None:
        while True:
            self.draw()
            self.process()
            self.handle_events()
            self.clock.tick(c.FRAMERATE)


def main() -> None:
    App().run()


if __name__ == '__main__':
    main()