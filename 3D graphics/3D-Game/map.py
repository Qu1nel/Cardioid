from settings import *

text_map = (
    'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH',
    'H     HHHHHHH     H                                H',
    'H                 H HHH           H                H',
    'H    HHHHHH                  HHHHHHHHH     HH      H',
    'H         HHHHHHHHHH         H    H        HH      H',
    'H         H                  H    H                H',
    'H    HHHH H     H                                  H',
    'H               H       HHHHHH        HHHHH HH     H',
    'H               H            H          H          H',
    'H        H      H                       H          H',
    'H        H      H                       H          H',
    'H     HHHH      HHHHHHHHHHHHHHHH                   H',
    'H     H                 H                          H',
    'H                       H               H          H',
    'H           H           H               H          H',
    'H    HH HH      H       HHHHHH       HHHHHHHHHHHH  H',
    'H    H   H      H       HHHHHH                     H',
    'H    H   H      H            H                     H',
    'H    H   H      H                                  H',
    'H    HHHHH      HHHHHHHH                           H',
    'H               H                 HHHHHHHHHH       H',
    'H  H                                               H',
    'H  H     H       HHHHHHHH HH             HH        H',
    'H  H     H       H         H             HH        H',
    'H     HHHH       H HHHHHHHHH         H             H',
    'H        H                           H             H',
    'H                                  HHHHHH          H',
    'H                                    H             H',
    'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
)

world_map = {(y * TILE, x * TILE) for x, row in enumerate(text_map) for y, char in enumerate(row) if char != ' '}
