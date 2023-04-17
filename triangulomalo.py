from turtle import *
from colorsys import *
def pintarlevel(level):
    print("level", level)

def tracesegment(level, size):
    forward(size)

def sierpinski(level, size):
    if (level <=0):
        return
    
    tracesegment(level,size)
    right(120)
    tracesegment(level,size)
    right(120)
    tracesegment(level,size)
    right(120)
    
    forward(size/2)
    sierpinski(level-1,size/2)
    
size = 300
level = 5
sierpinski(level,size)
exitonclick()