import random
from sys import exit

import pygame as pg

import config as c


def quick_copy(lst):
    return [[cell.copy() for cell in row] for row in lst]


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

    def copy(self):
        return Cell(coord=self.coord, alive=self.alive)


class GameLife(object):
    def __init__(self, app, sc: pg.Surface):
        self.app = app
        self.sc = sc
        self.color_cell = c.COLOR_CELL
        self.previous_area = None
        self.area = [[Cell(coord=(x, y), alive=False) for x in range(self.app.width // c.SIZE_CELL)]
                     for y in range(self.app.height // c.SIZE_CELL)]

    def draw_area(self):
        normalized = lambda coord: tuple(i * c.SIZE_CELL for i in coord)
        for row in self.area:
            for cell in row:
                if cell.is_alive():
                    pg.draw.rect(surface=self.sc,
                                 color=c.COLOR_CELL,
                                 rect=pg.Rect(normalized(cell.coord), (c.SIZE_CELL - 2, c.SIZE_CELL - 2)))

    def revive_cluster(self, coord_cell=None):
        if coord_cell is None:
            random_cell = random.choice(random.choice(self.area))
            while random_cell.is_alive():
                random_cell = random.choice(random.choice(self.area))

            if random.randint(0, 1) == 1:
                random_cell.alive = True

            X, Y = random_cell.coord
        else:
            X, Y = coord_cell[0] // c.SIZE_CELL, coord_cell[1] // c.SIZE_CELL
            self.area[Y][X].alive = True

        for _x, _y in ((-1, 1), (0, 1), (1, 1), (1, 0)):
            try:
                self.area[Y + _y][X + _x].alive = bool(random.randint(0, 1)) and bool(random.randint(0, 1))
            except IndexError:
                pass
            try:
                self.area[Y - _y][X - _x].alive = bool(random.randint(0, 1)) and bool(random.randint(0, 1))
            except IndexError:
                pass

    def next_cycle(self):
        self.previous_area = quick_copy(self.area)
        for line in self.previous_area:
            for cell in line:
                number_living = 0
                X, Y = cell.coord
                for _x, _y in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                    try:
                        column, row = Y + _y if Y + _y > 0 else 0, X + _x if X + _x > 0 else 0
                        number_living += self.previous_area[column][row].is_alive()
                    except IndexError:
                        pass
                    try:
                        column, row = Y - _y if Y - _y > 0 else 0, X - _x if X - _x > 0 else 0
                        number_living += self.previous_area[column][row].is_alive()
                    except IndexError:
                        pass
                if cell.is_alive():
                    if number_living not in (2, 3):
                        x, y = cell.coord
                        self.area[y][x].alive = False
                else:
                    if number_living == 3:
                        x, y = cell.coord
                        self.area[y][x].alive = True


class App(object):
    def __init__(self):
        self.width, self.height = (c.WIDTH, c.HEIGHT)
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
        self.clock = pg.time.Clock()
        self.game_life = GameLife(self, self.screen)
        self.pause = False

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
                elif event.key == pg.K_SPACE:
                    self.pause = not self.pause
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.game_life.revive_cluster(coord_cell=event.pos)

    def process(self) -> None:
        if not self.pause:
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
