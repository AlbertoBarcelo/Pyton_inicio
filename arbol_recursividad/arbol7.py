from turtle import *
from colorsys import *
from random import randint, random, choice


def traceBranch(level, size, angle):
    pen_size = 2 + level*4
    pensize(pen_size)
    tono = 0.028
    saturacion = max((1-level/50), 0.01)
    brillo = max((0.25-level/50), 0.02)
    pencolor(hsv_to_rgb(tono, saturacion, brillo))
    pendown()
    left(angle/2)
    forward(size/2)
    left(angle/2)
    forward(size/2)


def traceLeaf():
    color = choice(["#558749", "#335f09", "#234106"])
    radius = randint(4, 8)
    angle = randint(0, 200)
    right(angle)
    pencolor(color)
    fillcolor(color)
    begin_fill()
    circle(radius, -180)
    left(90)
    forward(radius*2)
    left(90)
    end_fill()
    right(-angle)


def returnToBranchBase(size, angle):
    penup()
    forward(-size/2)
    right(angle/2)
    forward(-size/2)
    right(angle/2)


def tree(level, size, angle):
    if (level <= 6) and (random() < 0.05):
        traceBranch(level, size, angle)
        returnToBranchBase(size, angle)
        return  # ============================>
    if (level <= 0):
        traceLeaf()
        return  # ============================>

    # Pintar rama actual
    traceBranch(level, size, angle)

    # Pintar arbol izquierdo
    tree(level-1, size*0.85+randint(int(-size*0.3),
        int(size*0.3)), randint(angle-6, angle+6))

    # Pintar arbol derecho
    tree(level-1, size*0.85 + randint(int(-size*0.3),
        int(size*0.3)), -randint(angle-6, angle+6))

    returnToBranchBase(size, angle)

    # left(-angle)

bgcolor("black")
speed(0)
penup()
goto(0, -325)
pendown()
hideturtle()
left(65)



# tree(10, 50, 17)
tree(8, 95, 25)

exitonclick()