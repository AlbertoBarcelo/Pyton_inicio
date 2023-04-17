## searching function
def buscar_numero(array, longitud, numero):

    ## array index for iteration
    i = 0

    ## variables to track the search area
    ## initializing them with start and end indexes
    inicio = 0
    fin = longitud - 1

    ## iterating over the array
    while i < longitud:
        ## getting the index of the middle element
        mitad = (inicio + fin) // 2

        ## checking the middle element with required element
        if array[mitad] == numero:
            ## returning True since the element is in the array
            return True
        elif array[mitad] < numero:
            ## moving the start index of the search area to right
            inicio = mitad + 1
        else:
            ## moving the end index of the search area to left
            fin = mitad - 1
        i += 1
    return False


if __name__ == '__main__':
    ## initializing the array, length, and element to be searched
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    longitud = 10
    elemento_a_buscar = 5
    # element_to_be_searched = 11

    if buscar_numero(array, longitud, elemento_a_buscar):
        print(elemento_a_buscar, "encontrado")
    else:
        print(elemento_a_buscar, "no encontrado")