print("Ingrese la cantidad de cursos que lleva en el semestre")
cursos=int(input())
contador = 1 
suma_aprobados=0
suma_reprobados=0
suma_promedio = 0
cont_aprobado=0
cont_reprobado=0
while (contador<=cursos):
    print("Ingrese los resultados de la nota", contador)
    nota=int(input())
    if (nota<70):
        suma_reprobados=suma_reprobados+nota
        cont_reprobado+=1
    else:
        suma_aprobados=suma_aprobados+nota
        cont_aprobado+=1
    suma_promedio+=nota
    contador+=1

if (cont_aprobado==0):#EStas condiciones las agregue para evitar errores de division por cero. 
    prom_aprobados=0
else:
    prom_aprobados=(suma_aprobados/cont_aprobado)

if (cont_reprobado==0):
    prom_reprobados=0
else:
    prom_reprobados=(suma_reprobados/cont_reprobado)  
if (cursos==0):
    prom_total=0
else:
    prom_total=(suma_promedio/cursos)
print("La cantidad de notas aprobadas es", cont_aprobado)
print("La cantidad de notas reprobadas es", cont_reprobado)
print("El promedio de sus notas es", prom_total)
print("El promedio de sus notas aprobadas es", prom_aprobados)
print("El promedio de sus notas reprobadas es", prom_reprobados)
