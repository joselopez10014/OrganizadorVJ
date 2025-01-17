# Biblioteca de Aserciones
## Requisitos
La biblioteca de aserciones que se va a utilizar debería de cumplir los siguientes requisitos:
- Estandar: Se valorara si es la solución estandar ya que no tendra ningun problema debido a posibles actualizaciones ademas de facilitar la busqueda de información.
- Mantenimiento: Se busca que tenga actualizaciones frecuentes para evitar que se quede desactualizado y empiece a generar una deuda técnica
- Permite mock: Se valorara que permitan usar mock o alguna función similar para facilitar la creación de los test
## Opciones
Estas son las opciones entre las que se ha elegido la biblioteca:
- Unittest: Es una librería estandar de python. Permite la ejecución de test que comprueban las funciones, encuentran errores y facilitan el desarrollo. Esta integrada en python.
- Hamcrest: Es una librería que nos provee de una serie de matchers que podemos utilizar para escribir nuestros test con un lenguaje más cercano al natural de manera que se hacen más sencillos de comprender.
- Assertpy: es una biblioteca Python potente y sencilla que tiene como objetivo mejorar la legibilidad de los test.
## Elección
He seleccionado unittest debido a que es de la librería estandar de python lo que hace que no genere problemas al añadirla al proyecto, ademas al contrario que las otras dos bibliotecas, unittest nos permite usar la función mock para facilitar la creación de los test de la lógica de negocios.
