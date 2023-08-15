import math
import sys
from typing import Never

import pygame as pg  # type: ignore

from src.misc import AppType, Position, Singleton


class Cardioid(metaclass=Singleton):
    """Cardioid curve object class.

    Attributes:
        app: Application object (as TApp).
        radius: Cardioid radius value.
        num_lines: Cardioid number lines.
        position: The center of the cardioid position on the screen.
        counter: Counter for tracking cardioid color status.
        inc: Counter increment value for changing the cardioid color state.

    Methods:
        draw(self, /) -> None: Drawing Cardioid object on display by "self.app".

    """

    app: AppType
    radius: float
    num_lines: int
    position: Position
    counter: float
    inc: float

    def __init__(self, app: AppType) -> None:
        """Initializing a cardioid object."""
        self.app = app
        self.radius = 350.0
        self.num_lines = 150
        self.position = Position(x=self.app.screen.get_width() // 2, y=self.app.screen.get_height() // 2)

        self.counter = 0.0
        self.inc = 0.0

    def draw(self) -> None:
        """Draws (self) the figure on the screen."""
        time = pg.time.get_ticks()
        factor = 1 + 0.001 * time

        def _get_x(delta: float) -> int:
            return -int(self.radius * math.cos(delta)) + self.position.x

        def _get_y(delta: float) -> int:
            return int(self.radius * math.sin(delta)) + self.position.y

        self.radius = abs(math.sin(time * 0.008) - 0.5) * 15 + 350

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i

            start_position_line = Position(x=_get_x(theta), y=_get_y(theta))
            end_position_line = Position(x=_get_x(theta * factor), y=_get_y(theta * factor))

            color = "yellow"
            pg.draw.aaline(self.app.screen, color, start_position_line, end_position_line)


class App(metaclass=Singleton):
    """Application class for working with a window.

    Attributes:
        width: Window widths.
        height: Window heights.
        screen: Surface for drawing.
        clock: Tactics for fps.
        cardioid: Cardioid object.

    Methods:
        draw(self, /) -> None: Drawing windows with Cardioid on display.
        run(self, /) -> None: Run app.

    """

    width: int
    height: int
    screen: pg.SurfaceType
    clock: pg.time.Clock
    cardioid: Cardioid

    def __init__(self) -> None:
        """Initializing a App object."""
        self.width = 1600
        self.height = 900

        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

        self.cardioid = Cardioid(self)

    def draw(self) -> None:
        """Draws the screen and cardioid."""
        self.screen.fill("black")
        self.cardioid.draw()
        pg.display.update()

    def run(self) -> Never:
        """Draws the window in an infinite loop and also handles events from the user."""
        while True:
            self.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

            self.clock.tick(144)
