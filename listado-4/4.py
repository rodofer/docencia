"""
Solicitar números desde el teclado hasta que el 
usuario ingrese el valor cero. Luego, mostrar por 
pantalla la sumatoria de los números introducidos
"""

# Daniel Godoy
suma = 0

while True:
    numero = int(input("Ingrese un numero: "))

    if numero == 0:
        break

    suma += numero

print(f"La suma total de los numero es {suma}")