import turtle

import config


class Rules(object):
    """semi-dictionary, semi-list"""

    __slots__ = ('__list', '__dict')

    def __init__(self, keys: dict = None, **kwargs):
        if not keys and not kwargs:
            raise TypeError("Rules() takes 1 positional arguments but 0 was given")
        if keys is None and kwargs:
            keys = kwargs
        elif keys and kwargs:
            keys = keys | kwargs

        for key in keys:
            if isinstance(key, (int, float)):
                raise ValueError("The keys can't be 'int' or 'float'")

        self.__dict = keys
        self.__list = list(keys)

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

    def get_result(self):
        for gen in range(self.gens):
            self.axiom = self.apply_rules()

    def apply_rules(self):
        return ''.join([self.rules[char] for char in self.axiom])


class App(object):
    def __init__(self, rule: Rules = Rules(config.rules['Honeycombs'])):
        self.width, self.height = (config.WIDTH, config.HEIGHT)
        self.__rules = rule
        self.l_system = LSystem(config.axiom, self.__rules, config.gens)
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
    def rules(self) -> Rules:
        return self.__rules

    @rules.setter
    def rules(self, rule: Rules) -> None:
        self.__rules = rule
        self.l_system = LSystem(config.axiom, self.__rules, config.gens)

    @property
    def turtle(self):
        return self.__kevin

    def draw(self) -> None:
        self.l_system.get_result()

        for char in self.l_system.axiom:
            if char == self.l_system.rules[0]:
                self.turtle.left(60)
                self.turtle.forward(config.step)
            elif char == self.l_system.rules[1]:
                self.turtle.right(60)
                self.turtle.forward(config.step)

    def run(self) -> None:
        turtle.pencolor('white')
        turtle.goto(-self.width // 2 + 60, -self.height // 2 + 60)
        turtle.clear()
        turtle.write(f'generation: {self.l_system.gens}', font=('Arial', 60, 'normal'))

        self.draw()

        self.screen.exitonclick()


if __name__ == '__main__':
    app = App()
    app.rules = config.rules['Honeycombs']
    app.run()
