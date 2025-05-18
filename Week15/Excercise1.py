# 1. Crea un `bubble_sort` por tu cuenta sin revisar el código de la lección.
# 2. Modifica el `bubble_sort` para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def homemade_bubble_sort(list):
    for outer_index in range(len(list)-1):
        for index in range (len(list)-1-outer_index):
            current_index=list[index]
            next_index=list[index+1]
            print(f'-- Iteracion {index}. Elemento actual: {current_index}, Siguiente elemento: {next_index}')
            if current_index>next_index:
                list[index]=next_index
                list[index+1]=current_index
    return list

list=homemade_bubble_sort([3,7,5,4,2,7,1,1])
print(list)

def inverted_bubble_sort(list):
    for outer_index in range(len(list)-1):
        for index in range (len(list)-1-outer_index):
            current_index=list[(len(list))-index-1]
            next_index=list[(len(list))-index-2]
            print(f'-- Iteracion {index}. Elemento actual: {current_index}, Siguiente elemento: {next_index}')
            if current_index<next_index:
                list[(len(list))-index-1]=next_index
                list[(len(list))-index-2]=current_index
    return list

list=inverted_bubble_sort([3,7,5,4,2,7,1,1])
print(list)