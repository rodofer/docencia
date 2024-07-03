import random, csv
import config

def generar_codigo():
    return random.randint(1000, 9999)

def menu():
    num_opcion = 1
    for opc in config.opciones_menu:
        print(f"{num_opcion}. {opc}")
        num_opcion += 1
    while True:
        try:
            seleccion = int(input("Opción: "))
            break
        except:
            print("El valor debe ser numérico")
    return seleccion

def registrar_trabajador(lista):
    codigo = generar_codigo()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo: ")
    sueldo_bruto = input("Sueldo bruto: ")

    lista.append([codigo, nombre, apellido, cargo, sueldo_bruto])

def listar_trabajadores(lista):
    print("Codigo\tNombre\tApellido\tCargo\tSueldo")
    for trab in lista:
        print(f"{trab[0]}\t{trab[1]}\t{trab[2]}\t\t{trab[3]}\t{trab[4]}")

def crear_planilla(lista, cargo):
    try:
        with open("dato.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Codigo", "Nombre", "Apellido", "Cargo", "Sueldo bruto"])
            if cargo == "todos":
                escritor.writerows(lista)
            else:
                for trabajador in lista:
                    if trabajador[3] == cargo:
                        escritor.writerow(trabajador)
        print("La planilla fue creada con éxito|")
    except:
        print("Ha ocurrido un error al crear la planilla")