Algoritmo parque_diversiones
    // DEFINICION DE VARIABLES
    Definir cantidad_personas, edad Como Entero
    Definir contador_nino, contador_adulto, contador_adulto_mayor Como Entero
    Definir tarifa_nino, tarifa_adulto, tarifa_adulto_mayor Como Entero
    Definir total_pago_nino, total_pago_adulto, total_pago_adulto_mayor, total_general, descuento Como Entero

    // INICIALIZACION DE CONTADORES
    contador_nino = 0
    contador_adulto = 0
    contador_adulto_mayor = 0

    // DEFINICION DE TARIFAS
    tarifa_nino = 4500
    tarifa_adulto = 8500
    tarifa_adulto_mayor = 5000

    Escribir "¿Cuantas personas van a ingresar?"
    Leer cantidad_personas

    // CICLO SE REPITE SEGUN CANTIDAD DE PERSONAS
    Para contador_persona=1 Hasta cantidad_personas Hacer
        Escribir "Ingresa edad de persona ", contador_persona
        Leer edad

        // SI EDAD ES MENOR O IGUAL A 13
        Si edad <= 13 Entonces
            contador_nino = contador_nino + 1
        FinSi

        // SI EDAD ES MAYOR O IGUAL A 14 Y MENOR O IGUAL A 64
        Si edad >= 14 Y edad <= 64 Entonces
            contador_adulto = contador_adulto + 1
        FinSi

        // SI EDAD ES MAYOR O IGUAL A 65
        Si edad >= 65 Entonces
            contador_adulto_mayor = contador_adulto_mayor + 1
        FinSi
    FinPara

    // CALCULOS DE PAGO POR CATEGORIA
    total_pago_nino = contador_nino * tarifa_nino
    total_pago_adulto = contador_adulto * tarifa_adulto
    total_pago_adulto_mayor = contador_adulto_mayor * tarifa_adulto_mayor

    // SUMATORIA DE LOS PAGOS POR CATEGORIA
    total_general = total_pago_nino + total_pago_adulto + total_pago_adulto_mayor

    // SI TOTAL GENERAL ES MAYOR O IGUAL A 30 MIL SE GENERA DESCUENTO DEL 10%
    Si total_general >= 30000 Entonces
        descuento = total_general * 0.10
    SiNo
        descuento = 0
    FinSi

    total_pago = total_general - descuento

    Escribir "---------------------"
    Escribir " COMPROBANTE DE PAGO "
    Escribir "---------------------"
    Escribir "Nino: ", contador_nino, " $", total_pago_nino
    Escribir "Adulto: ", contador_adulto, " $", total_pago_adulto
    Escribir "Adulto mayor: ", contador_adulto_mayor, " $", total_pago_adulto_mayor
    Escribir "---------------------"
    Escribir "Total general: $", total_general
    Escribir "Descuento: $", descuento
    Escribir "Total a pagar: $", total_pago
    Escribir "---------------------"
FinAlgoritmo