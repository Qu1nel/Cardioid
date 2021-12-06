from sys import exit

import pygame as pg

import config as c


class GameLife(object):
    def __init__(self, sc: pg.Surface):
        self.sc = sc
        self.color_cell = c.COLOR_CELL


class App(object):
    def __init__(self):
        self.width, self.height = (c.WIDTH, c.HEIGHT)
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
        self.clock = pg.time.Clock()
        self.game_life = GameLife(self.screen)

    @staticmethod
    def handle_events() -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def process(self) -> None:
        pass

    def draw(self) -> None:
        pass

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
