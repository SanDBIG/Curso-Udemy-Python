'''Ejercicio 1

Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
'''

cadena = "Te quiero solo como amigo"
print(len(cadena))

print(cadena[0 : 2]) #Imprime los dos primeros caracteres
print(cadena[-3: ]) #Imprima los tres ultimos caracteres

print(cadena[: : 2]) #imprima cada dos caracteres

print(cadena[: : -1]) #imprima cadena en sentido inverso

print(cadena[ :25] + cadena[:: -1]) #imprima cadena en un sentido y sentido inverso
