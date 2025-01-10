# Gestor de tareas
## Requisitos
Para seleccionar el gestor de tareas se han seguido estos criterios:
- Simplicidad: El gestor de tareas no debería de ser demasiado complejo para facilitar su comprensión y su uso durante el desarrollo.
- Fácil de aprender: debido a que este proyecto es simple el gestor debería de ser fácil de aprender y usar para no añadir una carga innecesaria al proyecto.
- Soporte: Se valorara que tenga una comunidad activa y buena documentación para que pueda facilitar la resolución de problemas. 
## Opciones
Python tiene varias opciones para usar como gestor de tareas entre las que se encuentran:
- Make: make es una herramienta clásica para automatizar tareas, basada en el archivo llamado Makefile. Aunque no es específica de Python, es ampliamente utilizada en el desarrollo de software. Es simple para proyectos sencillos y tiene una gran comunidad de usuarios. No es específico de python y su sintaxis puede volverse confusa.
- Fabric: Fabric es una herramienta orientada a la automatización de tareas locales y remotas, utilizando SSH. Esta centrado en la administración de sistemas remotos, por lo que puede ser mas compleja que las demás opciones.
- Task: Task es una herramienta simple de automatización de tareas escrita en go. Es fácil de usar, sin embargo es menos conocido que otras opciones.
- Just: just es un gestor de tareas moderno inspirado en make. Aunque no está limitado a Python, es ideal para automatizar tareas comunes. Tiene una sintaxis clara y es flexible en cuanto a lenguajes.
## Elección
Fabric se descarta debido a que tiene una mayor complejidad que no es necesaria para este proyecto. Eso nos deja con make, task y just los cuales son simples y fáciles de usar. Para este proyecto voy a usar Make debido a que es una opción fácil de usar y aprender, muy conocido por lo que sera mas fácil de comprender para los usuarios y ademas tiene buen soporte con mucha documentación en caso de problemas.