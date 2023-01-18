# hacer que la suma de dos valores de la lista de 14 en este caso
""" valor = 14
i = [2, 3, 4, 5, 6, 7, 8, 9, 12, 11]

for j in range(0, len(i)):
    for k in range(i+1, len(i)):
        if (i[j] + i[k]) == valor:
            print(i[j]+i[k])


lista = [1, 2, 3, 4]
print()
print(lista)
print()
print(lista[0:])
print(lista[0:1])
print(lista[0:2])
print(lista[0:3])
print(lista[0:4])
print()
print(lista[-1])
print()
print(lista[:-1])
print(lista[-3:])
print(lista[-4:4])
print(lista[-4:]) """
import random
from datetime import datetime
lista = []

valor = random.randint(0, 200000)

for i in range(0, 30000):
    lista.append(random.randint(0, 80000))

resultados = []
time_start = datetime.now()
for idx in range(0, len(lista)):
    for idx2 in range(idx+1, len(lista)):
        if (lista[idx] + lista[idx2]) == valor:
            resultados.append([lista[idx], lista[idx2]])

time_stop = datetime.now()
elapse_1 = time_stop - time_start

print(valor)
print(elapse_1)


# diccionario ejemplo
dic = {}
for num in lista:
    dic[num] = True

for num in lista:
    complemento = valor - num
    if complemento in lista:
        resultados.append
