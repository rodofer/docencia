# PARQUE DE DIVERSIONES
En un parque de diversiones, se necesita implementar un programa para vender boletos.

1. El programa debe consultar la cantidad de personas que van a ingresar al parque.

2. Existen 3 categorías de boletos con diferentes tarifas según la edad:

    | Categoría    | Valor  | Edad                   |
    |--------------|--------|------------------------|
    | Niño         | $4.500 | Hasta 13 años          |
    | Adulto       | $8.500 | Desde 14 hasta 64 años |
    | Adulto mayor | $5.000 | Desde 65 años          |

3. El programa debe registrar la edad de cada persona para determinar su tarifa y el pago general de los boletos.

4. Si el pago general es mayor o igual a $30.000, el programa debe calcular un descuento del 10% sobre ese total y generar el pago final.

5. El programa debe mostrar por pantalla un Comprobante de Pago como en el siguiente ejemplo:
    ~~~
     COMPROBANTE DE PAGO 
    ---------------------
    Niño: 1 $4500
    Adulto: 1 $8500
    Adulto mayor: 0 $0
    ---------------------
    Total general: $13000
    Descuento: $0
    Total a pagar: $13000
    ---------------------
    ~~~