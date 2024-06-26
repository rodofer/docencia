import random
import config

def codigo_azar():
    return random.randint(100000, 999999)

def validar_rut(rut_ingresado):
    if rut_ingresado == "":
        print("El rut es obligatorio")
        return False
    else:
        return True

def validar_correo(correo_ingresado):
    if correo_ingresado != "":
        return True
    else:
        print("El correo es obligatorio")
        return False

def menu():
    print("1. VIP")
    print("2. Galeria")
    print("3. Cancha")
    opcion = input("Opción: ")
    return opcion

def generar_boleta(cant_vip, cant_galeria, cant_cancha):
    with open("boleta.txt", "w") as archivo:
        if cant_vip != 0:
            codigo = codigo_azar()
            archivo.write("****************************\n")
            archivo.write(f"Código: {codigo}\n")
            archivo.write("Tipo VIP\n")
            archivo.write("Marcianeke sinfónico\n")
            archivo.write(f"Cantidad entradas: {cant_vip}\n")
            archivo.write(f"Valor: ${config.tarifa['vip'] * cant_vip}\n")

        if cant_galeria != 0:
            codigo = codigo_azar()
            archivo.write("****************************\n")
            archivo.write(f"Código: {codigo}\n")
            archivo.write("Tipo Galeria\n")
            archivo.write("Marcianeke sinfónico\n")
            archivo.write(f"Cantidad entradas: {cant_galeria}\n")
            archivo.write(f"Valor: ${config.tarifa['galeria'] * cant_galeria}\n")

        if cant_cancha != 0:
            codigo = codigo_azar()
            archivo.write("****************************\n")
            archivo.write(f"Código: {codigo}\n")
            archivo.write("Tipo Cancha\n")
            archivo.write("Marcianeke sinfónico\n")
            archivo.write(f"Cantidad entradas: {cant_cancha}\n")
            archivo.write(f"Valor: ${config.tarifa['cancha'] * cant_cancha}\n")