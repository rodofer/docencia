from config import tarifa, descuento

def calculo_general(cant_nino, cant_adulto, cant_adu_may):
    total_nino = cant_nino * tarifa['boleto_nino']
    total_adulto = cant_adulto * tarifa['boleto_adulto']
    total_adu_may = cant_adu_may * tarifa['boleto_adu_may']
    total_general = total_nino + total_adulto + total_adu_may
    return total_general

def calculo_descuento(valor):
    descuento_valor = 0
    if valor >= descuento['monto_minimo']:
        descuento_valor = valor * descuento['porcentaje']
    return descuento_valor

def generar_comprobante(total_nino, total_adulto, total_adu_may):
    total_general = calculo_general(total_nino, total_adulto, total_adu_may)
    descuento = calculo_descuento(total_general)
    final = total_general - descuento
    with open('comprobante.txt', 'w') as archivo:
        archivo.write(" COMPROBANTE DE PAGO \n")
        archivo.write("---------------------\n")
        archivo.write(f"Niño: {total_nino} ${total_nino*tarifa['boleto_nino']}\n")
        archivo.write(f"Adulto: {total_adulto} ${total_adulto*tarifa['boleto_adulto']}\n")
        archivo.write(f"Adulto mayor: {total_adu_may} ${total_adu_may*tarifa['boleto_adu_may']}\n")
        archivo.write("---------------------\n")
        archivo.write(f"Total general: ${total_general}\n")
        archivo.write(f"Descuento: ${descuento:.0f}\n")
        archivo.write(f"Total a pagar: ${final:.0f}\n")
        archivo.write("---------------------")