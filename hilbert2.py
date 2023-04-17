from turtle import *
import colorsys


def traceSegment(level, size):
    pensize(level*3)

    pencolor(colorsys.hsv_to_rgb(0.4 + level/8 % 1, 1, 1))
    pendown()
    forward(size)


def hilbert(level, angle, size):
    if level == 0:
        return

    right(angle)

    hilbert(level - 1, -angle, size)
    traceSegment(level, size)

    left(angle)
    hilbert(level - 1, angle, size)
    traceSegment(level, size)

    hilbert(level - 1, angle, size)

    left(angle)
    traceSegment(level, size)
    hilbert(level - 1, -angle, size)

    right(angle)


speed(0)
penup()
goto(-500, -300)
# hideturtle()

level = 3
angle = -90
size = 80
hilbert(level, angle, size)

exitonclick()
