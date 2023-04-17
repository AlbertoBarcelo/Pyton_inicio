from turtle import *
from colorsys import *

def hilbert(level, angle, size):
    if level==0:
        return
    else:
        right(angle)
        hilbert(level-1, -angle, size)
        forward(size)
        
        left(angle)
        hilbert(level-1, angle, size)
        forward(size)
        
        
        hilbert(level-1, angle, size)
        
        left(angle)
        forward(size)
        hilbert(level-1, -angle, size)
        right(angle)
        


speed(0)
level = 10
angle = -90
size = 5
hilbert(level, angle, size)

exitonclick()