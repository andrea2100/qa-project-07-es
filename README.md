# Proyecto: Pruebas automatizadas para comprobar la funcionalidad de la aplicación web Urban.Routes.

## Descripción del proyecto:
- Este proyecto consiste en automatizar pruebas para comprobar la funcionalidad de la aplicación web Urban.Routes, mediante el desarrollo del metodo POM por sus siglas en Ingles: Page Object Model (Modelo de objetos de página).

## Descripción de las tecnologías y técnicas utilizadas.

- Entorno de desarrollo integrado (IDE): Pycharm (Community Edition), versión 2023.3.2.
- Lenguaje de programación Python, versión 3.12.1.
- Paquete pytest, versión 8.0.0.
- Se utilizó como técnica para ejecutar las pruebas el comando pytest.
- Paquete selenium, versión 4.17.2
- Método POM.
- Controlador para navegador Chrome(). Versión 121.0.6167.161.

## Contenido de los archivos del proyecto:
- Archivo data.py. Este contiene todos los datos de entrada necesarios para la funcionalidad de la aplicación web Urban.Routes. 
- Archivo main.py. Este contiene el desarrollo del metodo POM con la clase UrbanRoutesPage, con los metodos que interactuan con los elementos y TestUrbanRoutes, donde se encuentran las funciones de pruebas de la aplicación web Urban.Routes.

## Instrucciones de cómo ejecutar las pruebas:

1. Configurar la dirección: Se localizaron los elementos correspondientes a los campos 'Desde' y 'Hasta' y se introdujeron las direcciones mediante el método de selenium "send_keys".
2. Seleccionar la tarifa Comfort: Se localizó el elemento de "tarifa comfort" y se seleccionó mediante el método de selenium "click".
3. Rellenar el número de teléfono: Se localizó el elemento del campo "número de teléfono" y se rellenó mediante el método de selenium "send_keys".
4. Agregar una tarjeta de crédito: Se localizó el elemento del campo "tarjeta de crédito" y se rellenó mediante el método de selenium "send_keys".
5. Escribir un mensaje para el controlador: Se localizó el elemento del campo "mensaje para el conductor" y rellenó mediante el método de selenium "send_keys".
6. Pedir una manta y pañuelos: Se localizó el elemento de "Manta y Pañuelos" y se seleccionó mediante el método de selenium "click".
7. Pedir 2 helados: Se localizó el elemento de "helados", se seleccionaron mediante el método de selenium "click".
8. Aparece el modal para buscar un taxi: Se localizó el elemento de "Pedir un taxi" y se seleccionó mediante el método de selenium "click".
9. Esperar a que aparezca la información del conductor en el modal: Se localizó el elemento de "información del conductor" mediante el método de espera hasta que aparezca un elemento "until(expected_conditions.visibility_of_element_located".

## Conclusiones:

**Luego de ejecutar las 9 pruebas se tiene como resultado:**

- Las 9 pruebas ejecutadas tuvieron un resultado positivo, en este caso se evidenció el correcto funcionamiento de la aplicación web Urban Routes, de acuerdo al alcance de este proyecto.