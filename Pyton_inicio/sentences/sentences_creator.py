#split() sirve para crear lista de palabras
# crear el diccionario

# meter las frases en una lista, luego las leemos y ponemos las palabras en un diccionario


# funcion para leer el archivo y separar las lineas
def meter_frases(sent):
    lista = []
    with open('Pyton_inicio-20230113T215612Z-001\Pyton_inicio\sentences\hola.txt') as sent:
        frases = sent.readlines()
        for line in frases:
            lista.append(line.strip('\n'))
    return lista
    lista = separadores(line)

# funcion para quitar los separadores 
def separadores(sep):
    sep = [',','.',';',':','-']
    for cambio in sep:
        sep = sep.replace(' ')

# funcion para leer la linea y sacar palabras
def leer(read):
    dic ={}
    

# crear diccionario


lista_frases = meter_frases('Pyton_inicio-20230113T215612Z-001\Pyton_inicio\sentences\hola.txt')
print(lista_frases)
