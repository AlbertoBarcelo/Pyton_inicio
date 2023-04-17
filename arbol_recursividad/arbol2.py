# Arbol
from turtle import *
from colorsys import *

def traceBranch(level, size, angle):

    pen_size = 2 + level*4
    pensize(level*5)

    tono = 0.3 - level*0.04
    saturacion = 1 - level*0.05
    brillo = 1 - level*0.15

    pencolor(hsv_to_rgb(tono, saturacion,brillo))

    left(angle)
    pendown()
    forward(size)


def returnToBranchBase(size, angle):
    penup()
    forward(-size)
    left(-angle)

def tree(level, size, angle=45):
    if (level<=0):
        return

    # Trazar una rama
    traceBranch(level, size, angle)

    tree(level-1, size, -angle)

    tree(level-1, size, angle)

    returnToBranchBase(size, angle)


#
# Main program
#
speed(0)
goto(0, -200)

bgcolor("black")

angle = 22
size = 80
level = 5
left(90-angle)
tree(level, size, angle)

exitonclick()
