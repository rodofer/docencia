"""
Solicitar un número desde el teclado y validar 
que sea positivo. En caso de no serlo,
volver a pedir el número hasta que supere 
la validación
"""

num = int(input("Ingresa un numero: "))

while num < 0:
    num = int(input("Ingresa un numero: "))
    print("El numero debe ser positivo")

# Hileok Hernandez
# while True:
#     num = int(input('ingrese el numero: '))

#     if num > 0:
#         print('es numero positivo.')
#         break
#     else:
#         print('no es positivo, vuelva a intentarlo')