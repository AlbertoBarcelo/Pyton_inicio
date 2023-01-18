import random
from datetime import datetime

lista = []
diccionario = {}

valor = random.randint(0, 200000)

for i in range(0, 30000):
    lista.append(random.randint(0, 80000))

resultados = []

time_start = datetime.now()
for idx in range(0, len(lista)):
    if not lista[idx] in diccionario:
        diccionario[lista[idx]] = []
        diccionario[lista[idx]].append(idx)

time_stop = datetime.now()
elapse_1 = time_stop - time_start

print(valor)
print(elapse_1)
print(len(diccionario))

print()

# sin optimizar
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

# deberes sacar resultados con un diccionario sin que se repita y fuardamos la posicion donde o hemos encontrado

l = [3, 2, 2, 1, 4]
num_resultados = []
