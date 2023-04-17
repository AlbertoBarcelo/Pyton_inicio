# Arbol
from turtle import *
from colorsys import *

def trace():
    return


def traceBranch(level, size):
    if (level<=0):
        trace(level,size)
        return
    triangulo= size/3
    
    traceBranch(level-1,triangulo)
    
    left(60)
    traceBranch(level-1,triangulo)
    
    right(120)
    traceBranch(level-1,triangulo)
    
    left(60)
    traceBranch(level-1,triangulo)


# Main program
#
speed(0)
goto(-200, -200)
bgcolor("black")
size = 300
level = 3
traceBranch(level, size)
exitonclick()
