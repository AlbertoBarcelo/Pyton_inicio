import random
def leer_archivo(ruta:str)-> object:
    try: 
        file  =  open(rf"{ruta}")
    except:
        print ("Hubo un error")
    else:
        return file


def limpiar(linea:str) ->str:
    separadores = {ord(','): '', ord(';'): '', ord(':'): '', ord('-'): '',ord('?'): '',ord('!'): '',}
    file= str(linea).translate(separadores)
    return file


def añadir(estado:tuple,word:str,dict_words): # type: ignore 
        if estado in dict_words:
            dict_words[estado].append(word)
        else:
            dict_words[estado] = [word]
        return dict_words


def crear_dict(ruta: str)-> dict: # type: ignore 
    file = leer_archivo(ruta)
    dict_words ={}
    for i in file :
        oracion_limpia = limpiar(i)
        list_words= oracion_limpia.rsplit()
        for j , word in enumerate(list_words):
            if j == 0:
                dict_words = añadir(("START","START"),word,dict_words)
                continue
            if j ==1:
                dict_words = añadir(("START",list_words[0]),word,dict_words)
                continue
            dict_words = añadir((list_words[j-2],list_words[j-1]),word,dict_words)
    return (dict_words)

# def frases(dict_words):
#         words = list()
#         estado = "START","START"
#         while True:
#             w = random.choice(dict_words[estado])
#             words.append(w)
#             estado = estado[1],w
#             if w.endswith("."):
#                 return " ".join(words)

def update_state (state:tuple[str],word:str)->tuple:
    state=state[1:]
    state = state + (word,)
    return state


dic = crear_dict('Pyton_inicio\sentences\hola.txt')

numero:int = int(input("¿Cuantas frases quieres?"))

# frases = frases(dic,numero)
# print(frases)


frases_ok={}
frase = list()
i = 1
state = "START","START"
status = state
while i < numero+1:
    word = random.choice(dic[state])
    frase.append(word)
    status = update_state(status,word)
    if not status in dic:
            frase_complet=" ".join(frase)
            if not frase_complet in frases_ok:
                print(f"{i}- "+ frase_complet,'\n')
                frases_ok[frase_complet]=i
                frase.clear()
                state= state
                i += 1
            else : 
                frase.clear()
                state = state
                

