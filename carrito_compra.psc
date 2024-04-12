Algoritmo carrito
    // DEFINICION DE VARIABLES
    Definir rut_cliente Como Caracter
    Definir opcion_menu_principal, cantidad, total_pago, efectivo, vuelto Como Entero
    Definir opcion_menu_secundario Como Entero
    Definir contador_peras Como Entero
    Definir contador_manzanas Como Entero
    Definir contador_naranjas Como Entero
    Definir precio_pera, precio_manzana, precio_naranja Como Entero
    Definir pago_peras, pago_manzanas, paga_naranjas Como Entero

    // INICIALIZACION DE CONTADORES
    contador_peras = 0
    contador_manzanas = 0
    contador_naranjas = 0

    // DEFINICION DE PRECIOS
    precio_pera = Aleatorio(100, 150)
    precio_manzana = Aleatorio(120, 165)
    precio_naranja = Aleatorio(80, 99)

    // INICIO CICLO MENU PRINCIPAL
    Repetir
        Escribir "1. Agregar producto"
        Escribir "2. Mostrar pedido"
        Escribir "3. Pagar"
        Escribir "4. SALIR"
        Leer opcion_menu_principal

        Segun opcion_menu_principal Hacer
            // AGREGAR PRODUCTO
            1:
                // INICIO CICLO MENU SECUNDARIO
                Repetir
                    Escribir "1. Pera"
                    Escribir "2. Manzana"
                    Escribir "3. Naranja"
                    Escribir "4. VOLVER"
                    Leer opcion_menu_secundario

                    Segun opcion_menu_secundario Hacer
                        1:
                            // SE VALIDA QUE CANTIDAD SEA MAYOR QUE CERO
                            Repetir
                                Escribir "¿Cuantas peras quieres?"
                                Leer cantidad
                            Hasta Que cantidad > 0
                            // CONTADOR SERA IGUAL AL VALOR ACTUAL DE CONTADOR
                            // MAS LA CANTIDAD RECIEN INGRESADA
                            contador_peras = contador_peras + cantidad

                        2:
                            // SE VALIDA QUE CANTIDAD SEA MAYOR QUE CERO
                            Repetir
                                Escribir "¿Cuantas manzanas quieres?"
                                Leer cantidad
                            Hasta Que cantidad > 0
                            // CONTADOR SERA IGUAL AL VALOR ACTUAL DE CONTADOR
                            // MAS LA CANTIDAD RECIEN INGRESADA
                            contador_manzanas = contador_manzanas + cantidad

                        3:
                            // SE VALIDA QUE CANTIDAD SEA MAYOR QUE CERO
                            Repetir
                                Escribir "¿Cuantas naranjas quieres?"
                                Leer cantidad
                            Hasta Que cantidad > 0
                            // CONTADOR SERA IGUAL AL VALOR ACTUAL DE CONTADOR
                            // MAS LA CANTIDAD RECIEN INGRESADA
                            contador_naranjas = contador_naranjas + cantidad

                        4:
                            Limpiar Pantalla
                    FinSegun
                // FIN CICLO MENU SECUNDARIO
                Hasta Que opcion_menu_secundario == 4 

            // MOSTRAR PEDIDO
            2:
                // SI SE AGREGO POR LO MENOS UNA PERA, MANZANA O NARANJA
                Si contador_peras <> 0 O contador_manzanas <> 0 O contador_naranjas <> 0 Entonces
                    Escribir "PEDIDO"

                    // SI SE AGREGARON PERAS AL CARRITO
                    Si contador_peras <> 0 Entonces
                        pago_peras = contador_peras * precio_pera
                        Escribir "Peras ", contador_peras, "X", precio_pera, "=", pago_peras
                    FinSi

                    // SI SE AGREGARON MANZANAS AL CARRITO
                    Si contador_manzanas <> 0 Entonces
                        pago_manzanas = contador_manzanas * precio_manzana
                        Escribir "Manzanas ", contador_manzanas, "X", precio_manzana, "=", pago_manzanas
                    FinSi

                    // SI SE AGREGARON NARANJAS AL CARRITO
                    Si contador_naranjas <> 0 Entonces
                        pago_naranjas = contador_naranjas * precio_naranja
                        Escribir "Naranjas ", contador_naranjas, "X", precio_naranja, "=", pago_naranjas
                    FinSi
                    // SI NO SE AGREGARON PRODUCTOS

                    total_pago = pago_peras + paga_naranjas + pago_naranjas
                    Escribir "TOTAL A PAGAR $", total_pago
                // SI NO SE AGREGARON PRODUCTOS
                SiNo
                    Escribir "El carrito esta vacio"
                FinSi

            // PAGAR
            3:
                // SI POR LO MENOS SE AGREGO UNA PERA, MANZANA O NARANJA
                Si contador_peras <> 0 O contador_manzanas <> 0 O contador_naranjas <> 0 Entonces
                    // SE VALIDA QUE RUT NO ESTE VACIO
                    Repetir
                        Escribir "Ingresa rut cliente"
                        Leer rut_cliente
                        Si rut_cliente == "" Entonces
                            Escribir "El campo Rut es obligatorio"
                        FinSi
                    Hasta Que rut_cliente <> ""

                    total_pago = pago_peras + paga_naranjas + pago_naranjas
                    Escribir "TOTAL A PAGAR $", total_pago

                    // SE VALIDA QUE EFECTIVO SEA MAYOR O IGUAL A TOTAL A PAGAR
                    Repetir
                        Escribir "Ingrese el efectivo"
                        Leer efectivo
                        Si efectivo < total_pago Entonces
                            Escribir "Efectivo no es suficiente"
                        FinSi
                    Hasta Que efectivo >= total_pago

                    vuelto = efectivo - total_pago
                    Escribir "Gracias por tu compra"
                    Escribir "Tu vuelto es $", vuelto

                    // SE RESETEAN LOS CONTADORES PARA VACIAR CARRITO
                    contador_peras = 0
                    contador_manzanas = 0
                    contador_naranjas = 0
                // SI NO SE AGREGARON PRODUCTOS
                SiNo
                    Escribir "El carrito esta vacio"
                FinSi
        FinSegun
    // FIN CICLO MENU PRINCIPAL
    Hasta Que opcion_menu_principal == 4
FinAlgoritmo
