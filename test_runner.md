# Test Runner
## Requisitos
La biblioteca de aserciones que se va a utilizar debería de cumplir los siguientes requisitos:
- Mantenimiento: Se busca que tenga actualizaciones frecuentes para evitar que se quede desactualizado y empiece a generar una deuda técnica.
- Claridad y extensión de los informes: Se valorara que los resultados de las pruebas sean claros y detallados, proporcionando información útil que facilite la identificación de fallos y su resolución.
Estas son las opciones entre las que se ha elegido el test runner:
- Unittest: Es el framework estándar de testing integrado en Python. Además de proporcionar herramientas para escribir aserciones y organizar pruebas, puede usarse como un test runner
- Pytest: Es un marco de trabajo de código abierto que permite a los desarrolladores escribir conjuntos de pruebas sencillos y compactos a la vez que admite pruebas unitarias, pruebas funcionales y pruebas de API. Es facil de usar y es el uno de lo mas usados y conocido por lo que que tiene una amplia comunidad y una gran cantidad de documentación. 
- Nose2: Es un ejecutor de pruebas popular en Python que puede detectar las pruebas unitarias en su proyecto y ejecutarlas. Tiene una comunidad menos activa que las demas opciones. 
## Elección
Nose2 es el que tiene el peor mantenimiento de los tres por lo que lo descarto. Entre Pytest y Unittest he elegido Pytest debido recibe actualizaciones de forma frecuente y ademas sus informes son mas detallados que los de unittest por defecto.
