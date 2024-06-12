import utils

cont_nino = 0
cont_adulto = 0
cont_adu_may = 0

cantidad_boletos = input("Ingresa cantidad de boletos: ")
while not cantidad_boletos.isdigit() or int(cantidad_boletos) <= 0:
    print("¡Debe ser un número positivo!")
    cantidad_boletos = input("Ingresa cantidad de boletos: ")

for i in range(int(cantidad_boletos)):
    edad = input(f"Edad (boleto {i+1}): ")
    while not edad.isdigit() or int(edad) <= 0:
        print("¡Debe ser un número positivo!")
        edad = input("Edad: ")

    if int(edad) <= 13:
        cont_nino += 1

    if int(edad) >= 14 and int(edad) <= 64:
        cont_adulto += 1

    if int(edad) >= 65:
        cont_adu_may += 1

utils.generar_comprobante(cont_nino, cont_adulto, cont_adu_may)