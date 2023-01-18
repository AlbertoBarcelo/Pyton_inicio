j = "hola" + \
    "me gustan las olass" + \
    "Hhooolaa comoo estass"
contador = 0
letras_anterior = "null"
letras_antepen = "null"
# for letras in j:
#  if letras == "a":
#     contador += 1
#print("letras'a'", contador)

# for letras in j:
#    if letras == "l" and letras_anterior == "o":
#        contador += 1
#    letras_anterior = letras
#print("contador", contador)

for letras in j:
    if letras == "a" and letras_anterior == "l" and letras_antepen == "o":
        contador += 1
    letras_antepen = letras_anterior
    letras_anterior = letras
print("contador", contador)
