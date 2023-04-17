import turtle

def arbol(longitud, t):
    if longitud > 2:
        t.forward(longitud)
        t.right(45)
        arbol(longitud-15, t)
        t.left(90)
        arbol(longitud-15, t)
        t.right(45)
        t.backward(longitud)


def main():
    t = turtle.Turtle()
    miVentana = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    arbol(75,t)
    miVentana.exitonclick()

main()