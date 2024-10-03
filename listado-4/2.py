"""
Solicitar la cantidad de números que el usuario desea introducir,
luego solicitar esos números y devolver por pantalla
el menor y el mayor de ellos
"""

# Miguel Villarroel
cant = int(input("Ingresa una cantidad\n-->"))
cont = 0

num = int(input("Ingresa un numero\n-->"))
mayor = num
menor = num

while cont < cant-1:
    #contador = contador + 1
    cont += 1
    num = int(input("Ingresa un numero\n-->"))

    if num > mayor:
        mayor = num

    if num < menor:
        menor = num

print(f"El numero mayor es {mayor} y el menor es {menor}")
