import turtle

import config


class Rules(object):
    """semi-dictionary, semi-list"""

    __slots__ = ('__list', '__dict', 'dict')

    def __init__(self, keys: dict = {}, **kwargs):
        for key in kwargs:
            if isinstance(key, (int, float)):
                raise ValueError("The keys can't be 'int' or 'float'")
        for key in keys:
            if isinstance(key, (int, float)):
                raise ValueError("The keys can't be 'int' or 'float'")

        self.__dict = keys if keys else kwargs
        self.__list = list(keys) if keys else list(kwargs)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__list[item]
        return self.__dict[item]

    def __repr__(self):
        parts = []
        for idx, key in enumerate(self.__dict.keys()):
            parts.append('{' f'{key}' '}' + f'[{idx}]: {self.__dict[key]}')
        res = ', '.join(parts)
        return 'Rules([{}])'.format(res)


class LSystem(object):
    def __init__(self, axiom: str = 'A', rules: dict = None, gens: int = 10):
        self.rules = Rules(A='AB', B='A') if rules is None else Rules(rules)
        self.axiom = axiom
        self.gens = gens

    def apply_rules(self):
        return ''.join([self.rules[char] for char in self.axiom])


class App(object):
    def __init__(self):
        self.width, self.height = (config.WIDTH, config.HEIGHT)
        self.l_system = LSystem(config.axiom, config.rules, config.gens)
        # screen settings
        self.screen = turtle.Screen()
        self.screen.setup(self.width, self.height)
        self.screen.screensize(3 * self.width, 3 * self.height)
        self.screen.bgcolor('black')
        self.screen.delay(0)
        # turtle settings
        self.__kevin = turtle.Turtle()
        self.__kevin.pensize(3)
        self.__kevin.speed(0)
        self.__kevin.color('yellow')

    @property
    def turtle(self):
        return self.__kevin

    def draw(self) -> None:
        self.turtle.setheading(0)
        self.turtle.goto(0, 0)
        self.turtle.clear()

        for char in self.l_system.axiom:
            if char == self.l_system.rules[0]:
                self.turtle.left(60)
                self.turtle.forward(config.step)
            elif char == self.l_system.rules[1]:
                self.turtle.right(60)
                self.turtle.forward(config.step)

        self.l_system.axiom = self.l_system.apply_rules()

    def run(self) -> None:
        for gen in range(self.l_system.gens):
            turtle.pencolor('white')
            turtle.goto(-self.width // 2 + 60, -self.height // 2 + 60)
            turtle.clear()
            turtle.write(f'generation: {gen}', font=('Arial', 60, 'normal'))

            self.draw()

        self.screen.exitonclick()


if __name__ == '__main__':
    App().run()
