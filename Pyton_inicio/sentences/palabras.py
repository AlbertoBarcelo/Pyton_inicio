
import random

# En esta funcion leemos el archivo y avisamos si no se ha podido.


def leer_archivo(ruta: str) -> object:
    try:
        file = open(rf"{ruta}")
    except:
        print("Hubo un error")
    else:
        return file

# Aqui lo que hacemos es quitar todo tipo de signos al texto para que nos sea mas facil tratar el texto posteriormente.


def limpiar(linea: str) -> str:
    separadores = {ord(','): '', ord(';'): '', ord('.'): '', ord(
        ':'): '', ord('-'): '', ord('?'): '', ord('!'): '', }
    file = str(linea).translate(separadores)
    return file

# Aqui lo que hacemos es añadir los estados a nuestro diccionario y creamos una lista con las palabra siguiente
# Comprobamos que el estado no este en nuestro diccionario y si lo esta añadimos la siguiente a la lista de nuestra clave 


def añadir(estado: tuple, word: str, dict_words): 
    if estado in dict_words:
        dict_words[estado].append(word)
    else:
        dict_words[estado] = [word]
    return dict_words


# En este paso utilizamos las funciones anteriores para crear nuestro diccionario
# Ademas detectamos el incio de cada frase y lo definimos com "START","START"

def crear_dict(ruta: str) -> dict:  
    file = leer_archivo(ruta)
    dict_words = {}
    dict_frases = {}
    for i in file:
        oracion_limpia = limpiar(i)
        dict_frases[oracion_limpia] = 0
        list_words = oracion_limpia.rsplit()
        for j, word in enumerate(list_words):
            if j == 0:
                dict_words = añadir(("START", "START"), word, dict_words)
                continue
            if j == 1:
                dict_words = añadir(("START", list_words[0]), word, dict_words)
                continue
            dict_words = añadir((list_words[j-2], list_words[j-1]), word, dict_words)
    return dict_words, dict_frases

# Lo que hacemos es actualizar el estado para luego a la hora de crear las frases seguir una coherencia

def update_state(state: tuple[str], word: str) -> tuple:
    state = state[1:]
    state = state + (word,)
    return state

# Aqui lo que hacemos es crear las frases gracias a nuestros estados
# Tambien comprobamos que las frases no se repiten gracias a que guradamos en un diccionario las frases que ya tenemos y hemos leido anteriormente
# Y con otro diccionario comprobamos que no generemos la misma frase dos veces

def gen_frases(dic: dict, F_Rep: dict, numero: int):
    frases_ok = {}
    frase = list()
    i = 1
    state = "START", "START"
    status = state
    while i < numero+1:
        word = random.choice(dic[status])  # aqui era status
        frase.append(word)
        status = update_state(status, word)
        if not status in dic:
            frase_complet = " ".join(frase)
            if (not frase_complet in frases_ok) and (not frase_complet in F_Rep):
                print(f"{i}- " + frase_complet, '\n')
                frases_ok[frase_complet] = i
                frase.clear()
                status = state  # status es quien vuelve al valor inicial
                i += 1
            else:
                frase.clear()
                status = state  # status es quien vuelve al valor inicial



numero: int = int(input("¿Cuantas frases quieres?: "))
print()
dic, F_rep = crear_dict('Programacion\Pyton_inicio-20230113T215612Z-001\Pyton_inicio\sentences\sentence_list_432.txt')
gen_frases(dic, F_rep, numero)
#hola