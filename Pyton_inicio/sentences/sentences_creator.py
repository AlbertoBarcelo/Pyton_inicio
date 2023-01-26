#split() sirve para crear lista de palabras
# crear el diccionario

# meter las frases en una lista, luego las leemos y ponemos las palabras en un diccionario



def meter_frases(sent):
    lista = []
    with open('Pyton_inicio-20230113T215612Z-001\Pyton_inicio\sentences\hola.txt') as sent:
        frases = sent.readlines()
        for line in frases:
            lista.append(line.strip('\n'))
    return lista

def separadores(sep):
    string.punctuation
    sep = [',','.',';',':','-']
    espacio = sep.replace(' ')




lista_frases = meter_frases('Pyton_inicio-20230113T215612Z-001\Pyton_inicio\sentences\hola.txt')
print(lista_frases)


# funcion para quitar los separadores 
# funcion para leer la linea 
# crear diccionario
# leer el archivo

def separadores(sep):
