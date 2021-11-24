from typing import Tuple

import pygame as pg

from settings import *


class Player(object):
    def __init__(self):
        self.position = dict(x=player_pos[0], y=player_pos[1])
        self.angle = player_angle
        self.speed = player_speed
        self.sensitivity = 0.02

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position['y'] -= self.speed
        if keys[pg.K_s]:
            self.position['y'] += self.speed
        if keys[pg.K_d]:
            self.position['x'] += self.speed
        if keys[pg.K_a]:
            self.position['x'] -= self.speed
        if keys[pg.K_LEFT]:
            self.angle -= self.sensitivity
        if keys[pg.K_RIGHT]:
            self.angle += self.sensitivity

    @property
    def pos(self) -> Tuple:
        return self.position['x'], self.position['y']
