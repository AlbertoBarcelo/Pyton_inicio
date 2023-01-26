x = "Hola"
print(x)

Fruta = ["Banana", "Manzana", "Naranja"]
q, w, e= Fruta
print(q, w, e)

r = 5
t = 10
print(r+t)

y = "Hello, World!"
print(y[2:5])

u = "Hello, World!"
print(u[:5])

i = "Hello, World!"
print(i[5])

o = "Hello, World!"
print(0[-5:-2]) 

p = "Hello"
a = "World"
s = p + " " + a
print(s)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#se puede acceder a datos concretos de una lista
print(thislist[2:5])
print(thislist[1])
#cambiar elementos de una lista
thislist[1:3] = ["blackcurrant", "watermelon"]
#añadir elemento
thislist.append("orange")
#elegir  donde insertamos un elemento de una lista
thislist.insert(1, "orange")

#tuplas
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#diccionarios
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#cambiar valores
thisdict["year"] = 2018
# añadir valores
thisdict["color"] = "red"