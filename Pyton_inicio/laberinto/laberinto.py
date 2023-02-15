# resolver un laberinto 
# hay que devolver dos listas en plan abajo derecha con las direcciones que has recorrido y luego con las coordenadas
import os
import colorama
# lo primero que hacemps es limpiar las consola

# def validar( x, y ,array)
# if x< len(array) and y<len(array[0]) and x >=0 and y>=0 and array[x][y] !=0:
    # return True
# return False
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

def mover(array):
    posiciones = {}
    movimientos = []
    i = 0
    j = 0
    posicion= 1
    # casilla = (array[i][j])
    # def movimientos (casilla,array,des)
    #i,j = casilla
    #if i < len (array) and  not (i+1,j) in des[casilla]:
        #x+1 ,y
        #return 
    #...



    for i in range(5):
        for j in range(5):
            if array[i][j] != "0" and not casilla in posiciones:
                movimientos.append((i, j))
                if j <len(array[0])-1 and  array[i][j +1] != "0" :
                    casilla = array[i][j+1]
                elif  i < len(array) -1  and i + 1 < 5 and  array[i+1][j] != "0":
                    casilla = array[i+1][j]
                elif j >=0 and  array[i][j-1] != "0":
                    casilla = array[i][j-1]
                elif i>=0 and array[i-1][j] != "0"  :
                    casilla = array[i-1][j]
            posiciones[posicion] = movimientos
            posicion = posicion +1
    return posiciones



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
