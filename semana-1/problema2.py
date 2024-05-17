

try:
    numero = int(input("ingresa un numero: "))
    mensaje = "es un numero impar"

    if numero % 2 == 0:
        mensaje = "e sun numero par"

    print(mensaje)

except Exception as e:
    print(e)
