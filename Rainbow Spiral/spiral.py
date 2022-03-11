from turtle import *

title('Rainbow Spiral')
speed(0)
bgcolor('Black')
R, G, B = (255, 0, 0)

for i in range(510):
    colormode(255)
    if i < 85:
        G += 3
    elif i < 170:
        R -= 3
    elif i < 255:
        B += 3
    elif i < 340:
        G -= 3
    elif i < 425:
        R += 3
    else:
        B -= 3
    forward(25 + i)
    right(91)
    pencolor(R, G, B)

input()
