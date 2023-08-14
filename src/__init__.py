"""Cardioid - visualization of an interesting version of this curve in animation."""

import pygame as pg  # type: ignore

from src.main import App

pg.init()


def main() -> None:
    """Entry point to the game."""
    game = App()
    game.run()
