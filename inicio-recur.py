# bucle infinto son muy graves, hay que revisar siempre
# para solucionar esto metemos la llamada recursiva dentro de un if, la condicion ha de ser falso en algun momento para que no sea un bucle infinito "Condicion de final de recursividad" evita una iteracion infinita, sino se bloquea el programa.
# hay que ir alerta de no consumir todos los recursos de la maquina esto se podria hacer mediante muchas llamadas recursivas.

# HASTA CUANDO

# sumar los numeros del 1-5 de forma recursiva

# Opcion 1
def Consecutiva1(n):
    if n >= 1:
        suma= n + suma.Consecutiva1(n-1)
    return(suma)

# Opcion 2
def Consecutiva2(n):
    if n == 1:
        return 1
    suma= n + suma.Consecutiva2(n-1)
    return(suma)


# pintar arbol binario de nivel m
def pintar():
    return

def arbolBinario(nivell):

    if nivell == 1:
        pintar.arbolBinario()
        return
    pintar.ramaIzquierda(nivell-1)
    pintar.ramaDerecha(nivell-1)


# FACTORIALES

def factorial_iterativo(i):
    factorial = 1
    for factor_actual in range(2,i+1):
        factorial*=factor_actual
    return factorial

def factorial_recursivo_v2(i):
    if i>1:
        return i * factorial_recursivo_v2(i-1)
    return 1

def factorial_recursivo_v3(i):
    if i==1:
        return 1
    return i * factorial_recursivo_v3(i-1)


# FRASES CAPICUA ejercicios iterativo y recursivo
# ejercicio para buscar un numero separando en mitades busqueda binaria

def is_palindrome_recursive (frase, idx=0):
    l = len(frase)