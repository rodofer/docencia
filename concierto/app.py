import funciones as func

contador_vip = 0
contador_galeria = 0
contador_cancha = 0

rut = input("Ingresa rut: ")
while func.validar_rut(rut) == False:
    rut = input("Ingresa rut: ")

correo = input("Ingresa correo: ")
while not func.validar_correo(correo):
    correo = input("Ingresa correo: ")

while True:
    opcion = func.menu()

    # Entrada VIP
    if opcion == "1":
        contador_vip += 1

    # Entrada Galeria
    elif opcion == "2":
        contador_galeria += 1

    # Entrada Cancha
    elif opcion == "3":
        contador_cancha += 1

    else:
        print(f"La opción {opcion} es incorrecta")

    seguir = input("Quieres seguir? (si/no): ")
    while seguir != "si" and seguir != "no":
        seguir = input("Quieres seguir? (si/no): ")

    if seguir == "si":
        continue
    if seguir == "no":
        break

func.generar_boleta(contador_vip, contador_galeria, contador_cancha)