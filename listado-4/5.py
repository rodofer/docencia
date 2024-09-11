"""
Solicitar números desde el teclado hasta que el 
usuario ingrese el valor cero. Luego, mostrar por
pantalla el promedio de los números positivos
"""

# Maximiliano Villalobos
sumatoria=0
contador=0

while True:
    numero=int(input("ingrese sus numeros para pomediarlo: "))
    if numero == 0:
        break
    sumatoria+=numero
    contador+=1

print(f"su promedio: {sumatoria/contador:.1f}")