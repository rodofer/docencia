import funciones

listado = []

while True:
    opcion = funciones.menu()

    if opcion == 1:
        funciones.registrar_trabajador(listado)

    elif opcion == 2:
        funciones.listar_trabajadores(listado)

    elif opcion == 3:
        cargo = input("Cargo: ")
        funciones.crear_planilla(listado, cargo)

    elif opcion == 4:
        break

    else:
        print("Opción incorrecta")