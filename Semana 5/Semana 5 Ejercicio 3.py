lista = []
while True:
    print("Ingrese valor a la lista (ENTER para terminar): ")
    valor = input()
    if valor:
        lista.append((valor))
    else:
        break
primero=lista[0]
ultimo=lista[len(lista)-1]
lista[0]=ultimo
lista[len(lista)-1]=primero
print('La nueva lista es')
print (lista)