#Asignacion de variables random
entero1=5
string1="texto"
booleano1=True
booleano2=False
float1=3.14
lista1=["1","2","3"]
lista2=["4","5","6"]
tupla1=(1,2,3,4)
print("....asignacion de variables completa")

#Inician los test
#entero1+string1 Type error por ser distintas variables
print(entero1+float1) #Da como resultado un float. 
#print(lista1+entero1) Da error no puede concatenar un entero a una lista, debe ser otra lista
print(lista1+lista2) #Como resultado, concatena las listas para dar una nueva lista de 6 indices
#print(lista1+tupla1) Da error no puede concatenar una tupla a una lista
print(lista1*booleano2)#multiplicar la lista por false da como resultado una lista vacia. 
print(lista1*booleano1)#Da como resultado la misma lista
print(entero1*booleano2)#Da como resultado un 0, como si borra su valor. 
print(entero1+float1+booleano1)#Se suma el booleano como un 1. 
print(lista1[2]+string1)#concatenacion de strings
print(lista2[1]*booleano2)#Da como resultado un espacio en blanco, como si borra el valor del string.
print(booleano1+booleano2) #Da como resultado 1.
print(booleano1+booleano1)#Da como resultado 2
print(booleano2+booleano2)#da como resultado 0
print(booleano1+booleano1+booleano2+booleano1)#Da como resultado 3, lo que significa que la suma los interpreta como 1 y 0s

