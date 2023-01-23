import sys, traceback

dict = {"Isaac": 19, "Raul":19, "Marcos":23}



persona=""
while persona.lower()!="Fin":
    persona = input("Nombre de la persona que buscamos: ")
    #if persona in dict:
    #    print("Edad de Raul", dict[persona])
    #else:
    #   print("No sabemos la edad de esta persona")
    try:
        print("Edad de " +persona, dict[persona])
        print(3/0)
    except KeyError:
        print("No tenemos el nombre de esta persona")
    except:
        print("Otro tipo de error")
