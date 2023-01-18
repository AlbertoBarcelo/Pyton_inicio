# i = 1
# print(i)
# i = i+1
# print(i)


# def power(base: int, exp: int = 2) -> int:
#     return base**exp


# resultado = power(2, 8)
# print("result 2^8", resultado)

# print("result 2^9", power(2, 9))
# print("result 2^10", power(2, 10))

# resultado = power(exp=11, base=2)
# print(resultado)

# resultado = power(5)
# print(resultado)


# los objetos NO se pasan por referencia, NO HAY PASO POR REFERENCIA

l = ["a", "b", "c"]
a, b, c = l
print(a, b, c)

for i in range(1, len(l)+1):
    print(l[-i], end="")

print(l[3:0:-1])

#
k = l
m = l[0:2]
u = l.copy()
l[0] = "hola"
u[1] = "adios"

print(m)
print(k)
print(l)
print(u)

#


def modifi(lis1: list, lis2: list) -> None:
    lis1[0] = "hola"
    lis1 = lis2
    print(lis1)


modifi(l, m)
print(l)
print(m)
#
#
a, b = 1, "j"
print(a, b)
#
#


def returnmultiple():
    return 1, True, "Hola"


a, b, c = returnmultiple()

print(a, b, c)
