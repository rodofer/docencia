import csv

lista_trabajadores = []

def registrar(lista:list):
    while True:
        nombre = input("Nombre: ")
        # Si el nombre es alfabetico y tiene 6 o mas caracteres
        if nombre.isalpha() and len(nombre) >= 6:
            # Si se cumplen las condiciones, salimos del ciclo
            break
        else:
            print("El nombre debe ser alfabetico y debe tener por lo menos 6 caracteres")

    while True:
        cargo = input("Cargo: ")
        # Si el cargo es alfabetico y tiene 5 o mas caracteres
        if cargo.isalpha() and len(cargo) >= 5:
            break
        else:
            print("El cargo debe ser alfabetico y debe tener por lo menos 5 caracteres")

    while True:
        sueldo = input("Sueldo: ")
        if sueldo.isdigit() and len(sueldo) >= 6:
            break
        else:
            print("El sueldo debe ser numerico y tener por lo menos 6 digitos")

    lista.append([nombre, cargo, sueldo])

def listar(lista:list, cargo):
    for trabajador in lista:
        if trabajador[1] == cargo:
            print(f"Nombre: {trabajador[0]}")
            print(f"Cargo: {trabajador[1]}")
            print(f"Sueldo: ${trabajador[2]}")
            print(".."*20)

def reporte(lista, tipo):
    if tipo == "txt":
        with open("reporte.txt", "w") as archivo:
            archivo.write("Reporte de trabajadores \n")
            archivo.write("="*40+"\n")
            for trabajador in lista:
                archivo.write(f"Nombre: {trabajador[0]}\n")
                archivo.write(f"Cargo: {trabajador[1]}\n")
                archivo.write(f"Sueldo: {trabajador[2]}\n")
                archivo.write(f"."*20 +"\n")
    elif tipo == "csv":
        with open("reporte.csv", "w") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Nombre trabajador", "Cargo trabajador", "Sueldo trabajador"])
            for trabajador in lista:
                escritor.writerows([[trabajador[0], trabajador[1], trabajador[2]]])
    print("Reporte generado correctamente en archivo.txt")

while True:
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Generar reporte TXT")
    print("4. Generar reporte CSV")
    print("5. SALIR")
    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        registrar(lista_trabajadores)

    elif opcion == "2":
        cargo = input("Cargo: ")
        listar(lista_trabajadores, cargo)

    elif opcion == "3":
        reporte(lista_trabajadores, "txt")

    elif opcion == "4":
        reporte(lista_trabajadores, "csv")

    elif opcion == "5":
        break

    else:
        print("La opción ingresada es incorrecta")