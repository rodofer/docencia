Algoritmo carrito
    Definir opcion_menu_principal Como Entero
    Definir opcion_menu_secundario Como Entero

    Repetir
        Escribir "1. Agregar producto"
        Escribir "2. Mostrar pedido"
        Escribir "3. Pagar"
        Escribir "4. SALIR"
        Leer opcion_menu_principal

        Segun opcion_menu_principal Hacer
            1:
                Repetir
                    Escribir "1. Pera"
                    Escribir "2. Manzana"
                    Escribir "3. Naranja"
                    Escribir "4. VOLVER"
                    Leer opcion_menu_secundario

                    Segun opcion_menu_secundario Hacer
                        1:
                            Escribir "Pera"
                        2:
                            Escribir "Manzana"
                        3:
                            Escribir "Naranja"
                        4:
                            Escribir "Volviendo..."
                        De Otro Modo:
                            Escribir "La opción es incorrecta"
                    FinSegun
                Hasta Que opcion_menu_secundario == 4
            2:
                Escribir "Mostrar pedido"
            3:
                Escribir "Pagar"
            4:
                Escribir "Saliendo..."
            De Otro Modo:
                Escribir "La opción es incorrecta"
        FinSegun
    Hasta Que opcion_menu_principal == 4
FinAlgoritmo