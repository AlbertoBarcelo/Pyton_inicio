from turtle import *
from colorsys import *

def pintar(level,size):
    if (level==0):
        return
    forward(size)

def sierpinski(level,size):
    if (level==0):
        return
    sierpinski(level-1,size/2)
    pintar(level,size)
    right(120)
    sierpinski(level-1,size/2)
    pintar(level,size)
    right(120)
    sierpinski(level-1,size/2)
    pintar(level,size)
    right(120)
    

size = 300
level = 3
sierpinski(level,size)
exitonclick()