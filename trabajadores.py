import random

listado = []

def generar_codigo():
    return random.randint(10000, 99999)

def solicitar_nombre():
    while True:
        nombre = input("Nombre: ")
        if nombre.isalpha() and len(nombre) >= 5:
            break
        else:
            print("El nombre debe tener por lo menos 5 letras")
    return nombre

def solicitar_apellido():
    while True:
        apellido = input("Apellido: ")
        if apellido.isalpha() and len(apellido) >= 5:
            break
        else:
            print("El apellido debe tener por lo menos 5 letras")
    return apellido

def solicitar_cargo():
    while True:
        cargo = input("Cargo: ")
        if cargo.isalpha() and len(cargo) >= 5:
            break
        else:
            print("El cargo debe tener por lo menos 5 letras")
    return cargo

def solicitar_sueldo():
    while True:
        sueldo = input("Sueldo: ")
        if sueldo.isdigit() and len(sueldo) >= 6:
            break
        else:
            print("El sueldo debe tener por lo menos 6 digitos")
    return sueldo

def agregar_trabajador():
    identificador = generar_codigo()
    nombre = solicitar_nombre()
    apellido = solicitar_apellido()
    cargo = solicitar_cargo()
    sueldo = solicitar_sueldo()
    listado.append([identificador, nombre, apellido, cargo, sueldo])

def modificar_trabajador():
    if len(listado) > 0:
        identificador = input("ID: ")
        registro_encontrado = False
        for i in range(len(listado)):
            if listado[i][0] == int(identificador):
                registro_encontrado = True
                break
        if registro_encontrado:
            listado[i][1] = solicitar_nombre()
            listado[i][2] = solicitar_apellido()
            listado[i][3] = solicitar_cargo()
            listado[i][4] = solicitar_sueldo()
    else:
        print("Todavia no hay registros")
   
def listar_trabajadores():
    for trabajador in listado:
        print(f"Código: {trabajador[0]}")
        print(f"Nombre: {trabajador[1]} {trabajador[2]}")
        print(f"Cargo: {trabajador[3]}")
        print(f"Sueldo: {trabajador[4]}")
        print("------------------")

def generar_reporte():
    if len(listado) > 0:
        with open("reporte.txt", "w") as archivo:
            archivo.write("Reporte de trabajadores\n")
            for trabajador in listado:
                # trabajador[0] es el Identificador
                archivo.write(f"Nombre: {trabajador[1]} {trabajador[2]}\n")
                archivo.write(f"Cargo: {trabajador[3]}\n")
                archivo.write(f"Sueldo: {trabajador[4]}\n")
    else:
        print("Todavia no hay registros")

while True:
    print("1. Agregar trabajador")
    print("2. Modificar trabajador")
    print("3. Listar trabajadores")
    print("4. Generar reporte")
    print("5. SALIR")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_trabajador()
    elif opcion == "2":
        modificar_trabajador()
    elif opcion == "3":
        listar_trabajadores()
    elif opcion == "4":
        generar_reporte()
    elif opcion == "5":
        break
    else:
        print("La opción es incorrecta")
