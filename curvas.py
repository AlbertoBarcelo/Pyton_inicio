import turtle
from colorsys import *


def koch(size, n):                  # Dibujar curva de Koch
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)



level = 2                  # Tres curvas de Koch se combinan en un copo de nieve de Koch
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
koch(400, level)
turtle.right(120)
koch(400, level)
turtle.right(120)
koch(400, level)
turtle.hideturtle()


