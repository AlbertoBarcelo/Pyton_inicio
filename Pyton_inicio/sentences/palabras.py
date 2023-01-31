#https://tech-es.netlify.app/articles/es510798/index.html#
import random

def read_file(documento):
    with open(documento) as frases:
        frases = frases.readlines()
        separadores = {ord(','): '', ord('.'): '', ord(';'): '', ord(':'): '', ord('-'): '',ord('?'): '',ord('!'): '',}
        frases= frases.translate(separadores)
        return frases


# def clean_lines(file):
#     separadores = {ord(','): '', ord('.'): '', ord(';'): '', ord(':'): '', ord('-'): '',ord('?'): '',ord('!'): '',}
#     file= file.translate(separadores)
#     return file


def read_lines(f:object)-> None:
    dict_words ={}
    for i in f:
        list_words:list[str]= f.rsplit()
        for i,words in enumerate(list_words): 
            if list_words[i] == words:
                dict_words[words] = list_words[i - 1]
            else:
                dict_words[words] = list_words[:i]
    return(dict_words)


file = read_file('Pyton_inicio\sentences\hola.txt')
clean = clean_lines(file)
dict = read_lines(clean)
print(dict)



# def read_file(path:str) ->object:
#     try:
#         file= open(path)
#     except:
#         print("Hubo un problema!!")
#     else:
#         return file


    

# def make_pairs(words):
#     for index in range(0, len(words)):
#         yield (words[index], words[index -state])
#         pair = make_pairs(words)
#     word_dict = {}
#     for word_1, word_2 in pair:
#         if word_1 in word_dict.keys():
#             word_dict[word_1].append(word_2)
#         else:
#             word_dict[word_1] = [word_2]
#     return word_dict



# print(List_pairs)

# no se pueden acepatar frases que ya estn en el diccionario ni frases repetidas a la hora de generarlas

# def crear_frase (chain, parts=2):
#     create = createinicalstate(state_parts)
#     word=""
#     word_list=[]
#     while true:
#         word = random.choice(chain[state])
#         if word == "stop":
#             break

    # word_list.append(word)

# def select_lines(li:object):
#     dict_words ={}
#     for line in range(0, len(li)):
#         j = li.rsplit()
#         for i in range(0,len(j)):
#             a = i-1
#             if line == 0:
#                 dict_words[line] = li[:a-1]
#             else:
#                 dict_words[line] = li[:a-1]
#             return(dict_words)