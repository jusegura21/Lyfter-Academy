def suma(valor1):
    print("Ingrese el valor que le desea sumar:")
    try:
        valor2=float(input())
        result=valor1+valor2
        return result
    except ValueError as error:
        print(f"No ha ingresado un numero valido:{error}")
        result = valor1
        return result
def resta(valor1):
    print("Ingrese el valor que le desea restar:")
    try:
        valor2=float(input())
        result=valor1-valor2
        return result
    except ValueError as error:
        print(f"No ha ingresado un numero valido:{error}")
        result = valor1
        return result

def multi(valor1):
    print("Ingrese el valor que desea multiplicar por:")
    try:
        valor2=float(input())
        result=valor1*valor2
        return result
    except ValueError as error:
        print(f"No ha ingresado un numero valido:{error}")
        result = valor1
        return result

def divide(valor1):
    print("Ingrese el valor que desea dividir por:")
    try:
        valor2=float(input())
        result=valor1/valor2
        return result
    except ValueError as error:
        print(f"No ha ingresado un numero valido:{error}")
        result = valor1
        return result
    
def borrar():
    return 0

def main():
    valor=0.0
    while True:
        print("_ _ _ _")
        print("       ")
        print("  ", valor)
        print("_ _ _ _")
        print("Digite el nùmero de la operación que desea ejecutar y presione ENTER")
        print("1.SUMAR")
        print("2.RESTAR")
        print("3.MULTIPLICAR")
        print("4.DIVIDIR")
        print("5.BORRAR")
        print("6.SALIR")        
        try:
            seleccion=int(input())
            if seleccion==1:
                valor=suma(valor)
            elif seleccion==2:
                valor=resta(valor)
            elif seleccion==3:
                valor=multi(valor)
            elif seleccion==4:
                valor=divide(valor)
            elif seleccion==5:
                valor=borrar()
            elif seleccion==6:
                break
            else:
                print("Seleccione un numero que se encuentre en el menú, presione ENTER para continuar")
                input()

        except ValueError:
            print("Error de entrada, ingrese unicamente el numero del menú")
            print("Presione ENTER para continuar")
            input()

    print("HASTA LUEGO")
    return 

main()      