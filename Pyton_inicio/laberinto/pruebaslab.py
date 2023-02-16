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
    for x in range(len(array)):
        for y in range(len(array[x])):
            casilla = (x, y)
            me_muevo = movements(casilla, array, posiciones)
            posiciones[(x, y)] = me_muevo
    return posiciones


lab = laberinto()
pintarlab =pintar(lab)
movimientos =mover(lab)
print(movimientos)