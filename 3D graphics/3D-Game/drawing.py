import pygame as pg

from ray_casting import ray_casting
from settings import *

pg.init()


class Drawing(object):
    def __init__(self, sc):
        self.sc = sc
        self.font = pg.font.SysFont('Arial', 35, bold=True)

    def world(self, player_position, player_angle):
        ray_casting(self.sc, player_position, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, PURPLE)
        self.sc.blit(render, FPS_POS)
