def tabla_multiplicar_arr(taula: int):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(0, 10):
        a[i] = taula * (i+1)

    return a


print(tabla_multiplicar_arr(5))

#


def tabla_multiplicar_list(taula: int):
    a = []
    for f in range(0, 10):
        a.append(taula * (f+1))

    return a


print(tabla_multiplicar_list(6))

#
#
#

for t in range(100, 105):
    print("taula del", t, tabla_multiplicar_arr(t))

# Cambios de tipo
print(list("Hola")*3)
print(int("hola"))
