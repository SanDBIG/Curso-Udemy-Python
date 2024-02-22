'''Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

#Nota de las 3 practicas
P1 = float(input("Ingrese nota de practica 1: "))
P2 = float(input("Ingrese nota de practica 2: "))
P3 = float(input("Ingrese nota de practica 3: "))
#

PP = float(P1 + P2 + P3) / 3  #promedio de practicas

#Nota de los examenes
EP = float(input("Ingrese nota examen parcial: "))
EF = float(input("ingrese nota de examen final: "))
#

#Promedio final
PROM = float((PP + (2*EP) + (3*EF))) / 6
print("Tu promedio de practicas es:\n ", PP,
      "\n Y el promedio final es:\n ", PROM)
#
