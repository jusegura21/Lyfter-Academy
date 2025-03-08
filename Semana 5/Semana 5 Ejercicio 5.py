lista=[]
contador=0
while contador<10:
    print("Ingrese un numero para agregar a la lista")
    valor=int(input())
    lista.append(valor)
    contador+=1  
contador2=0
print(len(lista))
for n in range(len(lista)):
    current_value =lista[n]
    if n == 0:   
        mayor = lista[n]
    elif current_value>mayor:
            mayor=current_value
print (lista)
print('El numero mayor es', mayor)
