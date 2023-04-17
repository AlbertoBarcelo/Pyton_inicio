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
    
    if x < len(laberinto) and (x+1, y) not in decisiones[casilla_actual] and not (x+1,y) in decisiones['indications_of_movements']:
        decisiones['indications_of_movements'].append('Abajo')
        return (x+1, y)
    if x < len(laberinto) and (x, y+1) not in decisiones[casilla_actual]and not (x,y+1) in decisiones['indications_of_movements']:
        decisiones['indications_of_movements'].append('Derecha')
        return (x, y+1)
    if x < len(laberinto) and (x, y-1) not in decisiones[casilla_actual]and not (x,y-1) in decisiones['indications_of_movements']:
        decisiones['indications_of_movements'].append('izquierda')
        return (x, y-1)
    if x < len(laberinto) and (x-1, y) not in decisiones[casilla_actual]and not (x-1,y) in decisiones['indications_of_movements']:
        decisiones['indications_of_movements'].append('arriba')
        return (x-1, y)
    return (-1,-1) # Casilla no valida, para saber que no tengo movimientos.

def mover (laberinto, x_start,y_start,x_end, y_end):
    if ((x_entrada,y_entrada) == (x_end,y_end)): # Mi entrada es mi salida.
        return
    
    camino_final = [(x_start, y_start) ] # Agregaremos las posiciones validas por las que me he movido 
    visitadas = [] # Marcar casillas visitadas
    decisiones={'indications_of_movements':['Entrada'],'way':[(x_entrada,y_entrada)],'wait-desitions':[]} # Guardo las decisiones agotadas en cada casilla casilla : [decisiones.....] con un maximo de 4 que seran los posibles movientos.
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
                decisiones[casilla_actual].pop()
                decisiones['wait-desitions'].append(next_cell)
                decisiones['indications_of_movements'].pop()
                continue
        
        elif next_cell == (-1,-1) and len(decisiones['wait-desitions'])!=0 and len(decisiones['camino']) > 1:
            casilla_actual=decisiones['wait-desitions'].pop()
            camino_final.pop()
        elif next_cell == (-1,-1):
            print("No solucon")
            break

        if (len(decisiones['indications_of_movements'])>1):
            decisiones['indications_of_movements'].pop()
    
    return camino_final,decisiones['indications_of_movements']



#Metodo principal:
if __name__ == "__main__":

    filas:int = int(input("Numero de filas: "))
    columnas:int = int(input("Numero de columnas: "))

    x_entrada = int(input("x entrada: "))
    y_entrada = int(input("y entrada: "))
    x_salida = int(input("x salida: "))
    y_salida = int(input("y salida: "))
    obstaculos:list[tuple] = [(3,2),(1,2),(1,3),(1,4),(0,1),(3,2),(2,1),(3,3),(4,6),(6,2),(6,3),(8,5),(8,8),(6,4),(9,4)]
    laberinto_generado = generar_laberinto(filas,columnas,obstaculos)
    pintar_laberinto_generado(laberinto_generado)
    camino,decisiones = mover(laberinto_generado,x_entrada,y_entrada,x_salida,y_salida)
    print (camino)
    print()
    pintar_camino(camino, laberinto_generado)
    print()
    print(colorama.Fore.RESET +f'{decisiones}' )



