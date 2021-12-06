import pygame as pg

import config as c


class App(object):
    def __init__(self):
        self.width, self.height = (c.WIDTH, c.HEIGHT)
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
        self.clock = pg.time.Clock()
        self.game_life = None

    def handle_events(self):
        pass

    def process(self):
        pass

    def run(self):
        pass


def main() -> None:
    App().run()


if __name__ == '__main__':
    main()
