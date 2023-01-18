# Lista
li = ["a", "b"]
print(li)

# los elemntos de un diccionario no tienen orden y constan de dos elementos una llave y un valor

# Diccionario
dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964}
dict.update({"color": "red"})
#dict["color"] = "R", dict["color": "R":26, "B":46, "G":274]
print(dict["color"])
#print("R", dict["color"]["R"])

# dict.pop ["color"] lo que hacemos es quitar el elemento

for item in dict:
    print(item, "-", dict[item])
print()

# al igualar se convierte en el mismo elemento con diferente nombre estan por referencia
# los datos que no son atomicos no se guardan dentro de una variable sino que se guardan las referencias
dict2 = dict
dict2["new-key"] = "prueba"
print(dict2)
print()
print(dict)
print()
# copiar diccionario
dict2 = dict.copy()
dict2["new-value"] = "prueba"
print(dict2)
print()
print(dict)
