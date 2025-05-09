#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

#1. Mixins para agregar funcionalidad extra (como imprimir o guardar en archivo)
#2. Separar lógica de autenticación y autorización
#3.Extendiendo comportamiento sin modificar clases originales. 
# Ideal cuando no puedes (o no quieres) modificar clases base existentes.
#4 Ejemplo

class CanFly:
    def Fly(self):
        print("The animal can fly.")

class CanSwim:
    def Swim(self):
        print("The animal can swim")

class Duck(CanFly,CanSwim):
    def sound(self):
        print("Cuac cuac 🦆")

donald = Duck()
donald.sound()     
donald.Fly()      
donald.Swim()      