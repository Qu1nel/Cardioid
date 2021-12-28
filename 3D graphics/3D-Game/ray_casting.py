from math import sin, cos

import pygame as pg

from map import world_map
from settings import *


def ray_casting(surface, pos: tuple, angle: float):
    cur_angle = angle - HALF_FOV
    xO, yO = pos
    for ray in range(NUM_RAY):
        sin_a = sin(cur_angle)
        cos_a = cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xO + depth * cos_a
            y = yO + depth * sin_a
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= cos(angle - cur_angle)
                proj_height = PROJ_RATIO / depth
                c = 255 / (1 + depth * depth * 0.00005)
                color = (c, c, c)
                pg.draw.rect(surface, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE
