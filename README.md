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

- Archivo data.py:Este contiene todos los datos de entrada necesarios para la funcionalidad de la aplicación web Urban.Routes. 
- Archivo retrieve_phone_code.py: En este archivo se encuentra la función para devolver el código que se solicita despues de agregar un número de teléfono. 
- Archivo selector.py: Este contiene todos los elementos de la aplicación web necesarios para las pruebas. Se debe importar el modulo: from selenium.webdriver.common.by import By.
- Archivo urban_routes_page.py: Este contiene la clase UrbanRoutesPage con todos los métodos, con los cuales se interactua en las pruebas. Se deben importar los siguientes modulos: from selenium.webdriver.support import expected_conditions, from selenium.webdriver.support.wait import WebDriverWait  
- Archivo test_urban_routes.py: Este contiene la clase TestUrbanRoutes, donde se encuentran todas las funciones de pruebas de la aplicación web Urban.Routes. Se deben importar los siguientes modulos: from selenium import webdriver, from urban_routes_page import UrbanRoutesPage.

## Instrucciones de cómo ejecutar las pruebas:


- La ejecución paso a paso de estas pruebas se observan en el navegador Chrome mediante el controlador de selenium. 
- Para ejecutar las pruebas se utiliza el comando pytest. 
- Las pruebas son:

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