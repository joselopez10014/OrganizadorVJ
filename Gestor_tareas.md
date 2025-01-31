# Gestor de tareas
## Requisitos
Para seleccionar el gestor de tareas se han seguido estos criterios:
- Mantenimiento: Se busca que tenga actualizaciones frecuentes para evitar que se quede desactualizado y empiece a generar una deuda técnica
- Requisitos de instalación: Se valora que no requiera dependencias adicionales ni configuraciones previas para su uso
## Opciones
Python tiene varias opciones para usar como gestor de tareas entre las que se encuentran:
- [Make](https://www.gnu.org/software/make/): make es una herramienta clásica para automatizar tareas, basada en el archivo llamado Makefile. Aunque no recibe actualizaciones tan frecuentes como otras posibles opciones es lo suficiente estable como para poder usarse sin añadir deuda tecnica.
- [Invoke](https://www.pyinvoke.org/): Invoke es una biblioteca de Python para administrar subprocesos orientados a shell y organizar código Python ejecutable en tareas invocables por CLI. Lleva un tiempo sin recibir actualizaciones.
- [Task](https://github.com/go-task/task): Task es una herramienta fácil de usar y que recibe una gran cantidad de actualizaciones, sin embargo requiere la instalación de varias dependencias adicionales para poder usarse.
- [Just](https://github.com/casey/just): just es un gestor de tareas moderno inspirado en make. Aunque no está limitado a Python, es ideal para automatizar tareas comunes.
## Elección
He descartado Invoke debido a que lleva muco tiempo sin recibir actualizaciones. Los demas reciben actualizaciones frecuentes o son lo suficiente estables para no generar deuda tecnica. Para este proyecto voy a usar Make debido a que suele estar instalado por defecto en linux por lo que no sera necesario hacer instalaciones ni configuraciones adicionales para su uso.
