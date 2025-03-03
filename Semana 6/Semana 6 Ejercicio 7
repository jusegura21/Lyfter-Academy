def numero_primo(value):  #funcion que retorna true si el numero es primo.
    contador=1
    compare=0
    while contador<=value:
            if value%contador==0:
                compare+=1
                contador+=1
            else:
                contador+=1
    if compare==2:
        return True
    else:
        return False

def modificate_list(list): #funcion que crea una lista a partir de los numeros primos que encuentre
    new_list=[]
    for index in range(len(list)):
        if numero_primo(list[index]):
            new_list.append(list[index])
    return new_list

lista = [1,2,3,4,6,7,25,13,9,67,43,75]

print(modificate_list(lista))