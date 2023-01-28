def frases(star):
    separadores = {ord(','): ' ', ord('.'): ' ', ord(';'): ' ', ord(':'): ' ', ord('-'): ' ',ord('?'): ' ',ord('!'): ' ',}
    with open(star) as fra:
        fra = fra.read()
        fra = fra.translate(separadores)
        return fra

def palabras(sun):
    sun = sun.split()
    return sun

def dic(moon):
    diccionario={}
    idx = 0
    idx2 = idx -1
    lis=[]
    for idx in range (0, len(moon)):
        if not moon(idx) in diccionario:
            diccionario[moon[idx]:lis[idx2]].append()
        else:
            diccionario[:lis[idx2]].append()




list_sentences = frases('sentences\hola.txt')
list_words = palabras(list_sentences)
List_dic = dic(list_words)
print(List_dic)

