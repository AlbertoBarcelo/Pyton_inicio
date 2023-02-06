# En esta funcion leemos el archivo y avisamos si no se ha podido.
def leer_archivo(ruta:str)-> object:
    try: 
        file  =  open(rf"{ruta}")
    except:
        print ("Hubo un error")
    else:
        return file

# Aqui lo que hacemos es quitar todo tipo de signos al texto
def limpiar(linea:str) ->str:
    separadores = {ord(','): '', ord(';'): '', ord('.'): '', ord(':'): '', ord('-'): '',ord('?'): '',ord('!'): '',}
    file= str(linea).translate(separadores)
    return file

# Aqui lo que hacemos es añadir los estados a nuestro diccionario
def añadir(estado:tuple,word:str,dict_words): # type: ignore 
        if estado in dict_words:
            dict_words[estado].append(word)
        else:
            dict_words[estado] = [word]
        return dict_words


def crear_dict(ruta: str)-> dict: # type: ignore 
    file = leer_archivo(ruta)
    dict_words ={}
    dict_frases = {}
    for i in file :
        oracion_limpia = limpiar(i)
        dict_frases[oracion_limpia] = 0
        list_words= oracion_limpia.rsplit()
        for j , word in enumerate(list_words):
            if j == 0:
                dict_words = añadir(("START","START"),word,dict_words)
                continue
            if j ==1:
                dict_words = añadir(("START",list_words[0]),word,dict_words)
                continue
            dict_words = añadir((list_words[j-2],list_words[j-1]),word,dict_words)
    return dict_words, dict_frases


def update_state (state:tuple[str],word:str)->tuple:
    state=state[1:]
    state = state + (word,)
    return state

def gen_frases (dic:dict, F_Rep:dict, numero: int):
    frases_ok={}
    frase = list()
    i = 1
    state = "START","START"
    status = state
    while i < numero+1:
            word = random.choice(dic[status]) ## aqui era status
            frase.append(word)
            status = update_state(status,word)
            if not status in dic:
                    frase_complet=" ".join(frase) 
                    if (not frase_complet in frases_ok) and (not frase_complet in F_Rep): 
                        print(f"{i}- "+ frase_complet,'\n')
                        frases_ok[frase_complet]=i
                        frase.clear()
                        status= state ### status es quien vuelve al valor inicial 
                        i += 1
                    else : 
                        frase.clear()
                        status= state ### status es quien vuelve al valor inicial
#####

import random
numero:int = int(input("¿Cuantas frases quieres?: "))
print()
dic, F_rep = crear_dict('sentences\star_wars.txt')
gen_frases(dic,F_rep,numero)




