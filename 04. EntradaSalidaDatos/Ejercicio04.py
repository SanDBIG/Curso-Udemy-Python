'''Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>'''

Nombre = str(input("Ingrese su nombre: "))
Edad = int(input("Ingrese su edad: "))
Sexo = str(input("Ingrese su sexo: "))

print("Te llamas: {}\nTu edad es: {}\nTu sexo es: {}".format(Nombre.capitalize(), Edad, Sexo.capitalize()))