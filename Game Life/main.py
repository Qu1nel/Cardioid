import random
from sys import exit

import pygame as pg

import config as c


class Cell(object):
    def __init__(self, coord: tuple[int, int], alive: bool = False):
        assert len(coord) == 2
        self.alive = alive
        self.__x, self.__y = coord

    def __str__(self):
        return 'Cell(alive={} coord={})'.format(self.alive, self.coord)

    def is_alive(self):
        return self.alive

    @property
    def coord(self):
        return self.__x, self.__y


class GameLife(object):
    def __init__(self, app, sc: pg.Surface):
        self.app = app
        self.sc = sc
        self.color_cell = c.COLOR_CELL
        self.area = [[Cell(coord=(x, y), alive=False) for x in range(self.app.width // c.SIZE_CELL)]
                     for y in range(self.app.height // c.SIZE_CELL)]

    def draw_area(self):
        normalized = lambda coord: [i * c.SIZE_CELL for i in coord]
        for row in self.area:
            for cell in row:
                if cell.is_alive():
                    pg.draw.rect(surface=self.sc,
                                 color=c.COLOR_CELL,
                                 rect=pg.Rect(normalized(cell.coord), (c.SIZE_CELL - 2, c.SIZE_CELL - 2)))

    def revive_cluster(self):
        random_cell = random.choice(random.choice(self.area))
        while random_cell.is_alive():
            random_cell = random.choice(random.choice(self.area))

        if random.randint(0, 1) == 1:
            random_cell.alive = True

        X, Y = random_cell.coord

        for _x, _y in ((-1, 1), (0, 1), (1, 1), (1, 0)):
            try:
                self.area[Y + _y][X + _x].alive = True if random.randint(1, 4) == 2 else False
            except IndexError:
                pass
            try:
                self.area[Y - _y][X - _x].alive = True if random.randint(1, 4) == 2 else False
            except IndexError:
                pass

    def next_cycle(self):
        for row in self.area:
            for cell in row:
                number_living = 0
                X, Y = cell.coord
                for _x, _y in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                    try:
                        number_living += 1 if self.area[Y + _y][X + _x].is_alive() else 0
                    except IndexError:
                        pass
                    try:
                        number_living += 1 if self.area[Y - _y][X - _x].is_alive() else 0
                    except IndexError:
                        pass
                if cell.is_alive():
                    if number_living not in (2, 3):
                        cell.alive = False
                else:
                    if number_living == 3:
                        cell.alive = True


class App(object):
    def __init__(self):
        self.width, self.height = (c.WIDTH, c.HEIGHT)
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
        self.clock = pg.time.Clock()
        self.game_life = GameLife(self, self.screen)

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
                elif event.key == pg.K_RETURN:
                    self.game_life.revive_cluster()

    def process(self) -> None:
        self.game_life.next_cycle()

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
