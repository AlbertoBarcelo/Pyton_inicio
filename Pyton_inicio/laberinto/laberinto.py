# resolver un laberinto 
# hay que devolver dos listas en plan abajo derecha con las direcciones que has recorrido y luego con las coordenadas

import os
# lo primero que hacemps es limpiar las consola
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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
