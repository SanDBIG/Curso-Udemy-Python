'''Ejercicio 3

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

VocalMinuscula = str(input("Ingrese vocal EN MINUSCULA: "))
LetraMayuscula = str(input("Ingrese consonante EN MAYUSCULA: "))

print("Vocal y letra juntas: ", VocalMinuscula.lower() + LetraMayuscula.upper())