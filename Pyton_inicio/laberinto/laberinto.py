import os
import colorama

# Primero deseo mostrar el laberinto con sus muros...
def pintar_laberinto_generado(laberinto: list[list[int]]):
    for i in range(len (laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 0:
                print(colorama.Fore.RED + str(laberinto[i][j]), end=" ")
                continue
            print(colorama.Fore.WHITE + str(laberinto[i][j]), end=" ")
            colorama.Style.RESET_ALL
        print()

# Aqui muestro mi solucion .....
def pintar_camino (solucion:list[tuple],laberinto: list[list[int]]):
    for i in range(len (laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 0:
                print(colorama.Fore.RED + str(laberinto[i][j]), end=" ")
                continue
            if (i,j) in solucion:
                print(colorama.Fore.GREEN + str(laberinto[i][j]), end=" ")
                continue
            print(colorama.Fore.WHITE + str(laberinto[i][j]), end=" ")
            colorama.Style.RESET_ALL
        print()

def generar_laberinto(filas, columnas, obstaculos):
    laberinto: list[list[int]] = [[1]*columnas for i in range(filas)]
    for i in range(filas):
        for j  in range(columnas):
            if (i,j) in obstaculos:
                laberinto[i][j]=0
        
    return laberinto        


def validar(next_cell, laberinto):
    x,y=next_cell
    if (x >= 0 and x < len(laberinto)) and (y >= 0 and y < len(laberinto[0])) and (laberinto[x][y] != 0):
        return True
    return False


def movements(casilla_actual, laberinto, decisiones:dict) ->tuple[int, int]:
    x, y = casilla_actual
    
    decisiones.setdefault(casilla_actual,[]) # Genera por defecto una clave u su valor por defecto.
    
    if x < len(laberinto) and (x+1, y) not in decisiones[casilla_actual]:
        return (x+1, y)
    if x < len(laberinto) and (x, y+1) not in decisiones[casilla_actual]:
        return (x, y+1)
    if x < len(laberinto) and (x, y-1) not in decisiones[casilla_actual]:
        return (x, y-1)
    if x < len(laberinto) and (x-1, y) not in decisiones[casilla_actual]:
        return (x-1, y)
    return (-1,-1) # Casilla no valida, para saber que no tengo movimientos.

def mover (laberinto, x_start,y_start,x_end, y_end):
    if ((x_entrada,y_entrada) == (x_end,y_end)): # Mi entrada es mi salida.
        return
    
    camino_final = [(x_start, y_start) ] # Agregaremos las posiciones validas por las que me he movido 
    visitadas = [] # Marcar casillas visitadas
    decisiones={} # Guardo las decisiones agotadas en cada casilla casilla : [decisiones.....] con un maximo de 4 que seran los posibles movientos.
    casilla_actual = (x_start, y_start) 
    
    # Buscar posibles soluciones mientras mi posicion no sea la salida, de ser asi , saldria de bucle.
    while  casilla_actual != (x_end,y_end):
        next_cell  = movements(casilla_actual, laberinto,decisiones) # le envias la casilla_actual actual a tu funcion y generas el proximo movimiento.
        decisiones[casilla_actual].append(next_cell)
        if validar(next_cell,laberinto): 
            if not next_cell in visitadas: # Verificamos que no este visitada esta casilla
                visitadas.append(casilla_actual)
                casilla_actual=next_cell
                camino_final.append(casilla_actual)                
                continue # Vamos a generar el siguiente moviento
            else:# En caso de estar visitada hago algo("Pendiente")
                pendiente = camino_final.pop()
                #Retroceder en caso de ser mi ultima alternativa.
                pass
        
        # Piensa como hacer que tu ultima decision sea retroceder.....
        # Pista puedes usar otros if ... condiciones ooooo   alguna estructura para tener constacia de que dejaste de dar un paso para ver otros 

        # if next_cell == (-1,-1) and #lista de espera esta vacia:
        #     return # No tengo posibles movientos      
        # else:
        #     casilla_actual = #lista de espera .pop
        
 
      


#Metodo principal:
if __name__ == "__main__":

    filas:int =  6      #int(input("Numero de filas: "))
    columnas:int = 5       #int(input("Numero de columnas: "))
    x_entrada = 0       #int(input("x entrada: "))
    y_entrada = 0       #int(input("y entrada: "))
    x_salida = 5       #int(input("x salida: "))
    y_salida = 4      #int(input("y salida: "))
    obstaculos:list[tuple] = [(2,3),(3,2),(1,2),(1,3),(1,4),(1,0),(0,1)]
    laberinto_generado = generar_laberinto(filas,columnas,obstaculos)
    pintar_laberinto_generado(laberinto_generado)
    mover(laberinto_generado,x_entrada,y_entrada,x_salida,y_salida)











#prueba


# primero creamos el laberinto que es una matriz con posiciones en la cada posicion creamos un (" ") para luego poder definir los muros
# para los muros recorremos el laberinto y donde hay un ladrillo le ponemos una x
#luego definimos la entrada y la salida del laberinto
# para pintar el laberinto recorremos la laberinto y dependiendo lo que encontemos lo pintamos de un color o otro colorama.back.color|| colorama.fore:color + texto hay que dar dos caracteres a cada casilla_actual para que sean cuadrados
# hay que usar la idea backtraking
# hay que guardar las casilla_actuals por las que ya he pasado
# funcion buscar el camino de salida
# hay que usar funciones dentro de otras funciones sitemas top down

# pasos 
# 1 hay que definir el laberinto 
# 2 hay que definir los muros
# 3 hay que definir la entrada y la salida
# 4 hay que guardar las casilla_actuals usadas en el programa
# 5 hay que definir los pasos a seguir: hay que tener en cuenta si hay un muro, si ya hemos pasado o si venimos de ahi
