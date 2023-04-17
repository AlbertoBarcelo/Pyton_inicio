from turtle import *
from colorsys import *

def tree(level=4, angle=45, size=100):
    #condicion de parada
    if(level==0):
        return
    
    pendown()
    left(angle)
    forward(size)
    
    # crear dos subarboles
    tree(level-1,angle, size)
    tree(level-1, -angle, size)

    forward(-size)
    left(-angle)


pendown()
goto(0,-200)

pencolor(hsv_to_rgb(0.3,1,1))
pensize(5)
bgcolor("black")
speed(1)
left(90-45)
tree(4,45,100)

angle=45
left(90-angle)
tree(4,angle,100)

exitonclick()