variable_global = 100

def suma_dos_valores (valor1,valor2):
    suma=valor1+valor2
    return suma

def suma_con_variable_global(valor1):
    variable_global=variable_global+valor1
    print(variable_global)


#main program
print("Test de variables globales y locales")
operacion = variable_global-suma #Resultado Name error: Suma is not defined. 
suma_con_variable_global(25) #resultado: UnboundLocalError: cannot access local variable 'variable_global' where it is not associated with a value


