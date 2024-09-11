"""
Solicitar la cantidad de número que el usuario desea introducir, 
luego solicitar esos números y devolver la sumatoria 
de los números impares
"""

# Miguel Villarroel
cant = int(input("Ingresa una cantidad\n-->"))
cont = 0
suma = 0

while cont < cant:
    #contador = contador + 1
    cont += 1

    num = int(input("Ingresa un numero\n-->"))

    #Si el numero es impar
    if num % 2 != 0:
        #sumatoria = sumatoria + numero
        suma += num

print(f"La suma de numeros impares es {suma}")