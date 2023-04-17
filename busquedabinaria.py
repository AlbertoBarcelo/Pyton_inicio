from random import randint


def crear_llista_ordenada(nombre_elements:int):
    llista_ordenada=[]
    for i in range(nombre_elements):
        llista_ordenada.append(randint(0,nombre_elements))
        

def cerca_binaria_iterativa(nombre_a_cercar:int,llista_ordenada:list):
    izq= 0
    der = len(llista_ordenada)-1
    cen=(izq+der)//2
    no_trobat= False
    
    while no_trobat & izq<=der:
        
        if izq>der:
            return False, None
        
        if llista_ordenada[cen]==nombre_a_cercar:
            return True, cen 
        "encontrado"
        #------------------------>
        
        if llista_ordenada[cen]>nombre_a_cercar:
            cerca_binaria_recursiva(nombre_a_cercar,llista_ordenada[izq:cen-1])
        else:
            cerca_binaria_recursiva(nombre_a_cercar,llista_ordenada[der:cen+1])
            izq=cen+1
            
        cen=(izq+der)//2
    
    
def test(nombre_a_cercar:int,llista_ordenada:int)->None:
        print("resultat iter", cerca_binaria_iterativa(nombre_a_cercar, llista_ordenada))
        print("resultat recur", cerca_binaria_recursiva(nombre_a_cercar, llista_ordenada))
        

def main():
    nombre_elements = 10
    llista_ordenada= crear_llista_ordenada(10)
    nombre_a_cercar= randint(0, nombre_elements)
    print("nombre a cercar ", nombre_a_cercar)
    test(nombre_a_cercar,llista_ordenada)
    print("resultat cerca", cerca_binaria_iterativa(nombre_a_cercar, llista_ordenada))




if __name__ == '__main__':
    main()
        