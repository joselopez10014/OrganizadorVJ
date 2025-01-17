# Gestor de tareas
## Requisitos
Para seleccionar el gestor de tareas se han seguido estos criterios:
- Mantenimiento: Se busca que tenga actualizaciones frecuentes para evitar que se quede desactualizado y empiece a generar una deuda técnica
- Eficiencia: Deben de ser rápidos a la hora de ejecutar las tareas.
## Opciones
Python tiene varias opciones para usar como gestor de tareas entre las que se encuentran:
- [Make](https://www.gnu.org/software/make/): make es una herramienta clásica para automatizar tareas, basada en el archivo llamado Makefile. Aunque no es específica de Python, es ampliamente utilizada en el desarrollo de software. Es simple para proyectos sencillos y tiene una gran comunidad de usuarios. No es específico de python y su sintaxis puede volverse confusa.
- [Invoke](https://www.pyinvoke.org/): Invoke es una biblioteca de Python para administrar subprocesos orientados a shell y organizar código Python ejecutable en tareas invocables por CLI.
- [Task](https://github.com/go-task/task): Task es una herramienta simple de automatización de tareas escrita en go. Es fácil de usar, sin embargo es menos conocido que otras opciones.
- [Just](https://github.com/casey/just): just es un gestor de tareas moderno inspirado en make. Aunque no está limitado a Python, es ideal para automatizar tareas comunes. Tiene una sintaxis clara y es flexible en cuanto a lenguajes.
## Elección
He descartado Invoke debido a que lleva tiempo sin recibir actualizaciones. Los demas reciben actualizaciones frecuentes o son lo suficiente estables para no generar deuda tecnica. Para este proyecto voy a usar Make debido a que es eficiente y ademas tiene buen soporte con mucha documentación en caso de problemas.
