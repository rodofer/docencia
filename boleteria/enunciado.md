# BOLETERIA
En un parque de diversiones, se necesita implementar un programa para vender boletos.

1. El programa debe consultar la cantidad de personas que van a ingresar al parque.

2. Existen 3 categorías de boletos con diferentes tarifas según la edad:

    | Categoría    | Valor  | Edad                   |
    |--------------|--------|------------------------|
    | Niño         | $4.500 | Hasta 13 años          |
    | Adulto       | $8.500 | Desde 14 hasta 64 años |
    | Adulto mayor | $5.000 | Desde 65 años          |

3. El programa debe registrar la edad de cada persona para determinar la tarifa de su boleto y el pago general de estos.

4. Si el pago general es mayor o igual a $30.000, el programa debe calcular un descuento del 10% sobre ese total y generar el pago final.

5. El programa debe generar un Comprobante de Pago como en el siguiente ejemplo:
    ~~~
    COMPROBANTE DE PAGO 
    ---------------------
    Niño: 2 $9000
    Adulto: 2 $17000
    Adulto mayor: 1 $5000
    ---------------------
    Total general: $31000
    Descuento: $3100
    Total a pagar: $27900
    ---------------------
    ~~~