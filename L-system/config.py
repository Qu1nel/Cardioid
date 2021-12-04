WIDTH = 1920
HEIGHT = 1000

gens = 13
rules = {
    'Honeycombs': ({'A': 'AB', 'B': 'A'}, 'A'),
    'Sierpinski triangle': ({'F': 'F-G+F+G-F', 'G': 'GG'}, 'F'),
    'Dragon curve': ({'X': 'X+YF+', 'Y': '-FX-Y'}, 'XY'),
    'Koch snowflake': ({'F': 'F-F++F-F'}, 'F++F++F'),
    'Tree': ({'X': 'F[+X]F[-X]+X', 'F': 'FF'}, 'X'),
    'Realistic Tree': ({'X': 'F[@[-X]+X]'}, 'X')
}
