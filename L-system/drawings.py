from random import randint


def _honeycombs(obj):
    angle = 60
    step = 50
    for char in obj.l_system.axiom:
        if char == obj.l_system.rules[0]:
            obj.turtle.left(angle)
            obj.turtle.forward(step)
        elif char == obj.l_system.rules[1]:
            obj.turtle.right(angle)
            obj.turtle.forward(step)


def _sierpinski_triangle(obj):
    angle = 120
    step = 8
    for char in obj.l_system.axiom:
        if char in (obj.l_system.rules[0], obj.l_system.rules[1]):
            obj.turtle.forward(step)
        elif char == '+':
            obj.turtle.right(angle)
        elif char == '-':
            obj.turtle.left(angle)


def _dragon_curve(obj):
    # gens = 12
    angle = 90
    step = 4
    for char in obj.l_system.axiom:
        if char in (obj.l_system.rules[0], obj.l_system.rules[1]):
            obj.turtle.forward(step)
        elif char == '+':
            obj.turtle.right(angle)
        elif char == '-':
            obj.turtle.left(angle)


def _koch_snowflake(obj):
    angle = 60
    step = 5
    for char in obj.l_system.axiom:
        if char == obj.l_system.rules[0]:
            obj.turtle.forward(step)
        elif char == '+':
            obj.turtle.right(angle)
        elif char == '-':
            obj.turtle.left(angle)


def _tree(obj):
    # gens 5
    step = 5
    angle = 22.5
    stack = []
    obj.turtle.left(90)
    obj.turtle.goto((0, -300))
    for char in obj.l_system.axiom:
        if char == obj.l_system.rules[1]:
            obj.turtle.forward(step)
        elif char == '+':
            obj.turtle.right(angle)
        elif char == '-':
            obj.turtle.left(angle)
        elif char == '[':
            angle_, pos_ = obj.turtle.heading(), obj.turtle.pos()
            stack.append((angle_, pos_))
        elif char == ']':
            angle_, pos_ = stack.pop()
            obj.turtle.setheading(angle_)
            obj.turtle.penup()
            obj.turtle.goto(pos_)
            obj.turtle.pendown()


def _realtree(obj):
    step = 90
    angle = lambda: randint(0, 38)
    color = [0.35, 0.2, 0.0]
    thickness = 20
    stack = []
    obj.turtle.left(90)
    obj.turtle.pensize(thickness)
    for char in obj.l_system.axiom:
        obj.turtle.color(color)
        if char in ('X', 'F'):
            obj.turtle.forward(step)
        elif char == '@':
            step -= 6
            color[1] += 0.04
            thickness -= 2
            thickness = max(1, thickness)
            obj.turtle.pensize(thickness)
        elif char == '+':
            obj.turtle.right(angle())
        elif char == '-':
            obj.turtle.left(angle())
        elif char == '[':
            angle_, pos_ = obj.turtle.heading(), obj.turtle.pos()
            stack.append((angle_, pos_, thickness, step, color[1]))
        elif char == ']':
            angle_, pos_, thickness, step, color[1] = stack.pop()
            obj.turtle.pensize(thickness)
            obj.turtle.setheading(angle_)
            obj.turtle.penup()
            obj.turtle.goto(pos_)
            obj.turtle.pendown()


def _gosper_curve(obj):
    angle = 60
    step = 3
    for char in obj.l_system.axiom:
        if char in (obj.l_system.rules[0], obj.l_system.rules[1], obj.l_system.rules[2]):
            obj.turtle.forward(step)
        elif char == '+':
            obj.turtle.right(angle)
        elif char == '-':
            obj.turtle.left(angle)


def _bush(obj):
    # gens 5
    step = 15
    angle = randint(18, 30)
    stack = []
    obj.turtle.left(90)
    for char in obj.l_system.axiom:
        if char == obj.l_system.rules[0]:
            obj.turtle.forward(step)
        elif char == '+':
            obj.turtle.right(angle)
        elif char == '-':
            obj.turtle.left(angle)
        elif char == '[':
            angle_, pos_ = obj.turtle.heading(), obj.turtle.pos()
            stack.append((angle_, pos_))
        elif char == ']':
            angle_, pos_ = stack.pop()
            obj.turtle.setheading(angle_)
            obj.turtle.penup()
            obj.turtle.goto(pos_)
            obj.turtle.pendown()


def _flower(obj):
    # gens 5
    step = 15
    angle = 30
    stack = []
    obj.turtle.left(90)
    obj.turtle.goto((0, -300))
    for char in obj.l_system.axiom:
        if char == obj.l_system.rules[0]:
            obj.turtle.forward(step)
        elif char == '+':
            obj.turtle.right(angle)
        elif char == '-':
            obj.turtle.left(angle)
        elif char == '[':
            angle_, pos_ = obj.turtle.heading(), obj.turtle.pos()
            stack.append((angle_, pos_))
        elif char == ']':
            angle_, pos_ = stack.pop()
            obj.turtle.setheading(angle_)
            obj.turtle.penup()
            obj.turtle.goto(pos_)
            obj.turtle.pendown()
