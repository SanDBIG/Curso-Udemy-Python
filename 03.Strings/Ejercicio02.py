'''Ejercicio 2

Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.'''

cadena = "separado"
caracter = ","

cadena_nueva = cadena.replace("", caracter).replace(caracter, "", 1)
print(cadena_nueva)