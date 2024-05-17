# escrive un programa que retorne la suma de 2 numeros
numero_1 = input("ingresa numero 1: ")
numero_2 = input("ingresa numero 2: ")


try: 
    suma = int(numero_1) + int(numero_2)
    print(suma)
except Exception as e: 
    print(e)    


