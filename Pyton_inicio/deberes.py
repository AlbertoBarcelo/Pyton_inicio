from datetime import datetime

lista = [3, 2, 2, 1, 4]
diccionario = {}
valor = 5

resultados = []
idx = 0

time_start = datetime.now()
for idx in range(0, len(lista)):
    complemento = valor - lista[idx]
    if complemento in diccionario:
        for idx1 in diccionario[complemento]:
            if idx1 > idx:
                resultados.append[
                    strResultados(
                        lista[idx], idx, complemento,idx1)]
                num_resultados += 1
                



time_stop = datetime.now()
elapse_1 = time_stop - time_start

print(valor)
print(elapse_1)
print(diccionario)
print (resultados)

print()
