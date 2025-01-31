# OrganizadorVJ
## Descripción del problema
Me dedico a recoger almendras para luego venderlas en alguna de las lonjas cercanas, para esto uso una página que me permite ver los precios de los distintos tipos de almendra en cada lonja.
El problema es que normalmente me interesa ver de forma clara como han ido variando los precios en los ultimos meses para decidir si debería de vender ya o esperar unos meses, pero eso es dificil de hacer en la página.
Me gustaria que hubiese alguna forma mas clara de ver la información de todas las lonjas. 
## Documentación
- [Documentación](./Documentacion)
- [Historias de usario](./Documentacion/Historias.md)
- [Milestones](./Documentacion/Milestones.md)
- [Gestor de Dependencias](./Documentacion/Gestor_dependencias.md)
- [Gestor de Tareas](./Documentacion/Gestor_tareas.md)
## Comprobar sintaxis
Se debe de usar esta orden: make check
## Test
Para realizar los tests usar: make test
## Docker
[Imagen elegida](./Documentacion/Imagen_docker.md)
Para construir el contenedor de forma local se usa este comando:
- docker build -t jose100/organizadorvj .
Para ejecutarlo se usa este comando:
- docker run -u 1001 -t -v `pwd`:/app/test jose100/organizadorvj
