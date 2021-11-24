__all__ = (
    'WIDTH', 'HEIGHT', 'FPS',
    'HALF_WIDTH', 'HALF_HEIGHT', 'TILE',
    'WHITE', 'BLACK', 'RED', 'GREEN', 'BLUE', 'DARKGRAY', 'PURPLE',
    'player_pos', 'player_angle', 'player_speed', 'sensitivity'
)
# game settings
FPS = 120
WIDTH = 1664
HEIGHT = 928
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
TILE = 32

# player
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2
sensitivity = 0.03

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
