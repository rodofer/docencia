"""
Solicitar por pantalla el ingreso de una contraseña por el teclado, si el valor
ingresado coincide con el valor definido en el programa, mostrar por pantalla “Sus
credenciales son correctas”. Sino, volver a solicitarla hasta que coincida. El usuario
tendrá tres intentos para introducir la contraseña correcta, después de superar los
intentos, el programa debe dejar de solicitar la contraseña y mostrar el mensaje “Su
cuenta ha sido bloqueada”
"""

# Diego Iturra
contraseña_correcta = "ilovemilfs"
intento_max = 3
intentos = 0

while intentos < intento_max:
    contraseña=input("Ingresar contraseña: ")

    if contraseña == contraseña_correcta:
        print("correcto mi rey")
        break
    else:
        intentos += 1

        if intentos < intento_max:
            print(f"Contraseña incorrecta, quedan {intento_max - intentos} intentos")
        else:
            print("Nao nao amiguinho, voce no pasa por acá")