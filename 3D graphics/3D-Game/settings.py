__all__ = (
    'WIDTH', 'HEIGHT',
    'HALF_WIDTH', 'HALF_HEIGHT',
    'WHITE', 'BLACK', 'RED', 'GREEN', 'BLUE', 'DARKGRAY', 'PURPLE',
    'player_pos', 'player_angle', 'player_speed'
)
# game settings
WIDTH = 1600
HEIGHT = 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# player
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
