"""
escribir un programa donde el usuario escriba un  texto y este lo invierta

ejemplo

hola -> aloh

"""


cadena = input("escriba el texto que desee invertir: ")

longitud = len(cadena)
cadena_invertida = ""

for indice in range(longitud - 1, - 1, - 1):
    cadena_invertida += cadena[indice]

print(cadena_invertida)
