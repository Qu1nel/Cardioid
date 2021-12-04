import sys

import pygame as pg

import config


class LSystem(object):
    def __init__(self, axiom: str = 'A', rules=None, gens: int = 10):
        self.rules = dict(A='AB', B='A') if rules is None else rules
        self.axiom = axiom
        self.gens = gens

    def apply_rules(self):
        result = []
        for char in self.axiom:
            result.append(self.rules[char])
        return ''.join(result)

    def process(self):
        for gen in range(self.gens):
            input()
            print(f'generation {gen}: {self.axiom}')
            self.axiom = self.apply_rules()


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
    LSystem(axiom=config.axiom, rules=config.rules, gens=config.gens).process()
    # App().run()
