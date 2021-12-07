import turtle

import config
import drawings as draw


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
        return ''.join([self.rules[char] if char in self.rules else char for char in self.axiom])


class App(object):
    def __init__(self, rule: Rules = Rules(config.rules['Honeycombs'][0])):
        self.width, self.height = (config.WIDTH, config.HEIGHT)
        self.mode = 'honeycombs'
        self.__rules = rule
        self.l_system = LSystem(config.rules['Honeycombs'][1], self.__rules, config.gens)
        self.screen = turtle.Screen()
        # screen settings
        self.screen.setup(self.width, self.height)
        self.screen.screensize(3 * self.width, 3 * self.height)
        self.screen.bgcolor('black')
        self.screen.delay(0)
        self.screen.title(f'generation: {config.gens}')
        # turtle settings
        self.__kevin = turtle.Turtle()
        self.__kevin.pensize(2)
        self.__kevin.speed(0)
        self.__kevin.setpos(0, -self.height // 2)
        self.__kevin.color('PURPLE')

    @property
    def rules(self) -> Rules:
        return self.__rules

    @rules.setter
    def rules(self, rule: str) -> None:
        self.__rules = config.rules[rule][0]
        self.l_system = LSystem(config.rules[rule][1], self.__rules, config.gens)
        self.mode = rule

    @property
    def turtle(self):
        return self.__kevin

    def draw(self) -> None:
        self.l_system.get_result()

        if self.mode.lower() == 'honeycombs':
            draw._honeycombs(self)
        elif self.mode.lower() == 'sierpinski triangle':
            draw._sierpinski_triangle(self)
        elif self.mode.lower() == 'dragon curve':
            draw._dragon_curve(self)
        elif self.mode.lower() == 'koch snowflake':
            draw._koch_snowflake(self)
        elif self.mode.lower() == 'tree':
            draw._tree(self)
        elif self.mode.lower() == 'realistic tree':
            draw._realtree(self)
        elif self.mode.lower() == 'gosper curve':
            draw._gosper_curve(self)
        elif self.mode.lower() == 'flower':
            draw._flower(self)
        elif self.mode.lower() == 'bush':
            draw._bush(self)

    def run(self) -> None:
        self.draw()
        self.screen.exitonclick()


if __name__ == '__main__':
    app = App()
    app.rules = 'Honeycombs'  # all rules in the config (module) in the rules (dict) + change gens
    app.run()
