WIDTH = 1600
HEIGHT = 900

gens = 9
rules = {
    'Honeycombs': ({'A': 'AB', 'B': 'A'}, 'A'),
    'Sierpinski triangle': ({'F': 'F-G+F+G-F', 'G': 'GG'}, 'F'),
    'Dragon curve': ({'X': 'X+YF+', 'Y': '-FX-Y'}, 'XY'),
    'Koch snowflake': ({'F': 'F-F++F-F'}, 'F++F++F'),
    'Plant': ({'X': 'F[+X]F[-X]+X', 'F': 'FF'}, 'X'),
    'RPlant': ({'X': 'F[@[-X]+X]'}, 'X')
}
