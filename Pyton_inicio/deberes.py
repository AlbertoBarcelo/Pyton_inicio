from datetime import datetime

lista = [3, 2, 2, 1, 4]
diccionario = {}
valor = 5

resultados = []
idx = 0
idx1 = idx + 1
time_start = datetime.now()
for idx in range(0, len(lista)):
    if not lista[idx] in diccionario:
        diccionario[lista[idx]] = []
        diccionario[lista[idx]].append(idx)
    if lista[idx] + lista[idx1] is valor:
        resultados = lista[idx] + lista[idx1]


time_stop = datetime.now()
elapse_1 = time_stop - time_start

print(valor)
print(elapse_1)
print(diccionario)
print (resultados)

print()
