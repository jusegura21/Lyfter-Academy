def sumatoria_de_lista(list_1):
    sumatoria=0
    for index in range(len(list_1)):
        sumatoria+=list_1[index]
    return sumatoria


my_first_list = [2, 5, 7, 8,22]
print (len(my_first_list))
print("El resultado de la sumatoria de los numeros de la lista es",sumatoria_de_lista(my_first_list))

