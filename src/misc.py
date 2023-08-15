from typing import Any, ClassVar, NamedTuple, Protocol

import pygame as pg  # type: ignore


class Position(NamedTuple):
    """Position for view x and y coord."""

    x: int
    y: int


class AppType(Protocol):
    """Protocol for App object."""

    screen: pg.SurfaceType

    def run(self) -> None:
        """Protocol method for run app."""
        ...

    def draw(self) -> None:
        """Protocol method for drawing app on display."""
        ...


class Singleton(type):
    """Class template singleton."""

    _instances: ClassVar[dict] = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any):  # type: ignore  # noqa: ANN204, D102
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
