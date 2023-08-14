import math
import sys
from typing import Never, Protocol

import pygame as pg  # type: ignore


class TApp(Protocol):
    """Protocol for App object."""

    screen: pg.SurfaceType

    def run(self) -> None:
        """Protocol method for run app."""
        ...

    def draw(self) -> None:
        """Protocol method for drawing app on display."""
        ...


class Cardioid:
    """Cardioid curve object class.

    Attributes:
        app: Application object (as TApp).
        radius: Cardioid radius value.
        num_lines: Cardioid number lines.
        position: The center of the cardioid position on the screen.
        counter: Counter for tracking cardioid color status.
        inc: Counter increment value for changing the cardioid color state.

    Methods:
        get_color(self, /) -> None: Gets a new color (pygame.Color) for cardioid.
        draw(self, /) -> None: Drawing Cardioid ojbect on display by "self.app".

    """

    app: TApp
    radius: float
    num_lines: int
    position: tuple[int, int]
    counter: float
    inc: float

    def __init__(self, app: TApp) -> None:
        """Initializing a cardioid object."""
        self.app = app
        self.radius = 350.0
        self.num_lines = 150
        self.position = (self.app.screen.get_width() // 2, self.app.screen.get_height() // 2)
        self.counter = 0.0
        self.inc = 0.0

    def get_color(self) -> pg.Color:
        """Rotates the new cardioid color (gradient) relative to the counter.

        Returns:
            pygame.Color

        """
        self.counter += self.inc

        if not (0 < self.counter < 1):
            self.counter, self.inc = (max(min(self.counter, 1), 0), -self.inc)

        return pg.Color("red").lerp("green", self.counter)

    def draw(self) -> None:
        """Draws (self) the figure on the screen."""
        time = pg.time.get_ticks()
        factor = 1 + 0.001 * time

        def _get_x(theta: float) -> int:
            return -int(self.radius * math.cos(theta)) + self.position[0]

        def _get_y(theta: float) -> int:
            return int(self.radius * math.sin(theta)) + self.position[1]

        self.radius = abs(math.sin(time * 0.008) - 0.5) * 15 + 350

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i

            x1 = _get_x(theta)
            y1 = _get_y(theta)

            x2 = _get_x(theta * factor)
            y2 = _get_y(theta * factor)

            pg.draw.aaline(self.app.screen, "yellow", (x1, y1), (x2, y2))  # 'yellow' = self.get_color()


class App:
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

            self.clock.tick(60)
