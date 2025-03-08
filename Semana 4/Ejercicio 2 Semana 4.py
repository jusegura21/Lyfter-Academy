print("Ingrese su nomnbe"),
nombre=input()
print("Ingrese su apellido")
apellido =input()
print("Ingrese su edad")
edad=int(input())
if (edad<=2):
    print(f'{nombre} {apellido} es un bebe')
elif (edad<=10):
    print(f'{nombre} {apellido} es un niño')
elif (edad<=15):
    print(f'{nombre} {apellido} es un preadolescente')
elif (edad<=18):
    print(f'{nombre} {apellido} es un adolescente')
elif (edad<=25):
    print(f'{nombre} {apellido} es un adulto joven')
elif (edad<=50):
    print(f'{nombre} {apellido} es un adulto')
else:
    print(f'{nombre} cle{apellido} es un adulto mayor')
