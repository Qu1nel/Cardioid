from typing import Tuple

import pygame as pg

from settings import *


class Player(object):
    __slots__ = 'x', 'y', 'angle', 'speed', 'sensitivity'

    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.speed = player_speed
        self.sensitivity = sensitivity

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= self.speed
        if keys[pg.K_s]:
            self.y += self.speed
        if keys[pg.K_d]:
            self.x += self.speed
        if keys[pg.K_a]:
            self.x -= self.speed
        if keys[pg.K_LEFT]:
            self.angle -= self.sensitivity
        if keys[pg.K_RIGHT]:
            self.angle += self.sensitivity

    @property
    def pos(self) -> Tuple:
        return self.x, self.y
