import os
import colorama

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def laberinto():
    laberinto = [
        ['e', '0', '0', '0', '0'],
        ['1', '1', '1', '0', '0'],
        ['0', '1', '1', '1', '1'],
        ['0', '1', '1', '1', '1'],
        ['0', '0', '0', '0', 's'],
    ]
    return laberinto

def pintar(array):
    colorama.init()
    for i in range(5):
        for j in range(5):
            if array[j][i] == '0':
                print(colorama.Back.RED + str(array[j][i]), end=" ")
            if array[j][i] == '1':
                print(colorama.Back.CYAN + str(array[j][i]), end=" ")
            if array[j][i] == 'e':
                print(colorama.Back.YELLOW + str(array[j][i]), end=" ")
            if array[j][i] == 's':
                print(colorama.Back.YELLOW + str(array[j][i]), end=" ")
        print()
        colorama.Style.RESET_ALL
    return array

def validar(x, y, array):
    if (x >= 0 and x < len(array)) and (y >= 0 and y < len(array[0])) and (array[x][y] != 0):
        return True
    return False

def movements(casilla, array, des):
    x, y = casilla
    if x < len(array) and (x+1, y) not in des[casilla]:
        if validar(x, y, array):
            return (x+1, y)
    if x < len(array) and (x-1, y) not in des[casilla]:
        if validar(x, y, array):
            return (x-1, y)
    if x < len(array) and (x, y+1) not in des[casilla]:
        if validar(x, y, array):
            return (x, y+1)
    if x < len(array) and (x, y-1) not in des[casilla]:
        if validar(x, y, array):
            return (x, y-1)

def mover(array):
    posiciones = {}
    x= 0
    y=0
    for x in range(len(array)):
        for y in range(len(array[x])):
            casilla = (x, y)
            me_muevo = movements(casilla, array, posiciones)
            posiciones[(x, y)] = me_muevo
    return posiciones

def buscar_inicio(array):
    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] == "e":
                inicio = array[x][y]
            y=y+1
        x=x+1
    return inicio


lab = laberinto()
pintarlab =pintar(lab)
movimientos =mover(lab)
print(movimientos)






# primero creamos el laberinto que es una matriz con posiciones en la cada posicion creamos un (" ") para luego poder definir los muros
# para los muros recorremos el array y donde hay un ladrillo le ponemos una x
#luego definimos la entrada y la salida del laberinto
# para pintar el laberinto recorremos la array y dependiendo lo que encontemos lo pintamos de un color o otro colorama.back.color|| colorama.fore:color + texto hay que dar dos caracteres a cada casilla para que sean cuadrados
# hay que usar la idea backtraking
# hay que guardar las casillas por las que ya he pasado
# funcion buscar el camino de salida
# hay que usar funciones dentro de otras funciones sitemas top down

# pasos 
# 1 hay que definir el array 
# 2 hay que definir los muros
# 3 hay que definir la entrada y la salida
# 4 hay que guardar las casillas usadas en el programa
# 5 hay que definir los pasos a seguir: hay que tener en cuenta si hay un muro, si ya hemos pasado o si venimos de ahi
