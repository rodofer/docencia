"""
Solicitar el ingreso de un nombre que tenga
por lo menos siete caracteres, en caso contrario,
volver a pedirlo hasta que el valor del nombre 
cumpla con el requisito
"""

# Diego Torres
while True:
    nombre = input("Ingrese un nombre valido:  ")

    if len(nombre) >= 7:
        print("Su nombre es valido")
        break
    else:
        print("Su nombre no es valido, intente nuevamente")