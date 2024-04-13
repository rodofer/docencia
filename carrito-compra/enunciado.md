# CARRITO DE COMPRA
En la tienda El Guatón de la fruta, se requiere implementar un programa que permita realizar ventas a sus trabajadores.
 
1. El programa debe desplegar un menú principal con las siguientes opciones:
    ~~~
    1. Agregar producto
    2. Mostrar pedido
    3. Pagar
    4. SALIR
    ~~~

2. En la opción `Agregar producto` del menú principal, el programa debe desplegar un menú secundario con las siguientes opciones:
    ~~~
    1. Pera
    2. Manzana
    3. Naranja
    4. VOLVER
    ~~~

3. El menú secundario debe repetirse hasta que se seleccione la opción `VOLVER` (al menú principal).

4. En la opción `Pera` del menú secundario, el programa debe preguntar la cantidad de peras que desea agregar al carrito de compra. La cantidad de peras debe ser un número mayor que cero.

5. En la opción `Manzana` del menú secundario, el programa debe preguntar la cantidad de manzanas que desea agregar al carrito de compra. La cantidad de manzanas debe ser un número mayor que cero.

6. En la opción `Naranja` del menú secundario, el programa debe preguntar la cantidad de naranjas que desea agregar al carrito de compra. La cantidad de naranjas debe ser un número mayor que cero.

7. En la opción `Mostrar pedido` del menú principal, el programa debe mostrar solo los productos agregados al carrito, como en el siguiente ejemplo:
    ~~~
    PEDIDO
    Manzana 2x550 = $1100
    Naranja 1x180 = $180
    TOTAL A PAGAR $1280
    ~~~
    - 7.1 El programa debe validar que existan productos en el carrito antes de mostrar el pedido. En caso contrario debe notificar al usuario con el mensaje "El carrito está vacío".

8. En la opción `Pagar` del menú principal, el programa debe validar que existen productos en el carrito antes de continuar con la compra. En caso contrario debe notificar al usuario con el mensaje "El carrito está vacío".
    - 8.1 El usuario debe ingresar el rut del cliente, este dato no puede ser un valor vacío.
    - 8.2 El programa debe mostrar por pantalla el total a pagar y debe solicitar la cantidad de efectivo para el pago. El valor del efectivo debe ser mayor o igual que el total a pagar.
    - 8.3 El programa debe mostrar por pantalla el mensaje “Pago realizado, gracias por tu compra” y “Tu vuelto es $X”, donde X es la diferencia entre el efectivo y el total a pagar.
    - 8.4 Una vez realizada la compra, el carrito debe quedar vacío.

9. El menú principal debe repetirse hasta que se seleccione la opción `SALIR` (del programa).

10. El precio de cada producto debe ser definido internamente dentro del programa en forma **aleatoria**.