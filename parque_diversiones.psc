Algoritmo parque_diversiones
	Definir cantidad_personas, edad, total_general, descuento, total_pagar Como Entero
	// Variables para almacenar los valores de las tarifas
	Definir tar_nino, tar_adulto, tar_adu_may Como Entero
	// Variables para contabilizar a las personas
	Definir con_nino, con_adulto, con_adu_may Como Entero
	// Variable para el total a pagar por categoria
	Definir total_pagar_nino, total_pagar_adulto, total_pagar_adu_may Como Entero
	
	// Se asigna el valor de las tarifas
	tar_nino = 4500
	tar_adulto = 8500
	tar_adu_may = 5000
	
	// Se inicializan los contadores
	con_nino = 0
	con_adulto = 0
	con_adu_may = 0

	Escribir Sin Saltar("Ingresa cantidad personas")
	Leer cantidad_personas
	
	Para contador=1 Hasta cantidad_personas Con Paso 1 Hacer
		Escribir "Ingresa edad persona ", contador
		Leer edad
		
		Si edad <=13 Entonces
			con_nino = con_nino + 1
			Escribir "El ni�o paga $", tar_nino
		FinSi
		
		Si edad >= 14 y edad <= 64 Entonces
			con_adulto = con_adulto + 1
			Escribir "El adulto paga $", tar_adulto
		FinSi
		
		Si edad >= 65 Entonces
			con_adu_may = con_adu_may + 1
			Escribir "El adulto mayor paga $", tar_adu_may
		FinSi
	FinPara
	
	total_pagar_nino = tar_nino*con_nino
	total_pagar_adulto = tar_adulto*con_adulto
	total_pagar_adu_may = tar_adu_may*con_adu_may
	
	Escribir "Comprobante de Pago"
	Escribir "-------------------"
	Escribir "Niño: ", con_nino, " $", total_pagar_nino
	Escribir "Adulto: ", con_adulto, " $", total_pagar_adulto
	Escribir "Adulto mayor: ", con_adu_may, " $", total_pagar_adu_may
	Escribir "-------------------"
	
	total_general = total_pagar_nino + total_pagar_adulto + total_pagar_adu_may
	Escribir "Total General: $", total_general
	
	Si total_general >= 30000 Entonces
		descuento = total_general * 0.10
	SiNo
		descuento = 0
	FinSi

	Escribir "Descuento: $", descuento
	total_pagar = total_general - descuento
	Escribir "Total a Pagar: $", total_pagar
FinAlgoritmo