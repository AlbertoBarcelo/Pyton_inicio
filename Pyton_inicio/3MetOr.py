import random
from datetime import datetime


print("¿Que tamano tiene la array?")
largo = input()

print("¿Cuantas veces lo hemos de revisar?")
veces = input()

array = []
len(largo)
contador = 0

numero_nuevo = random.randint(1, 50000)

while contador < int(largo):
    numero_nuevo = random.randint(1, 50000)
    if numero_nuevo in array:
        pass
    else:
        array.append(numero_nuevo)
        contador = contador+1

# Funciones
array1 = array.copy()
def burbuja(array1):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(array1)-1):
            if array1[i] > array1[i+1]:
                array1[i], array1[i+1] = array1[i+1], array1[i]
                intercambio = True

array2 = array.copy()
def seleccion(array2):
    longitud = len(array2)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if array2[i] > array2[j]:
                array2[i], array2[j] = array2[j], array2[i]

array3 = array.copy()
def insercion(array3):
    for i in range(len(array3)):
        for j in range(i, 0, -1):
            if (array3[j-1] > array3[j]):
                aux = array3[j]
                array3[j] = array3[j-1]
                array3[j-1] = aux
#
j= 0
while j < int(veces):
    j = j + 1
    print("Revision",j)
# Burbuja
    time_start1 = datetime.now()
    burbuja(array1)
    time_stop1 = datetime.now()
    elapse_1 = time_stop1 - time_start1
    print("Burbuja",elapse_1)


    # Seleccion
    time_start2 = datetime.now()
    seleccion(array2)
    time_stop2 = datetime.now()
    elapse_2 = time_stop2 - time_start2
    print("Seleccion",elapse_2)


    # Inserccion
    time_start3 = datetime.now()
    insercion(array3)
    time_stop3 = datetime.now()
    elapse_3 = time_stop3 - time_start3
    print("Inserccion",elapse_3)

# buscar forma para sumar todos los numeros de una lista grande