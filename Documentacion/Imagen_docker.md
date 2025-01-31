# Docker
## Requisitos
Estos son los requisitos que se han seguido para elegir la imagen docker:
- mantenimiento: Se busca que la imagen elegida se actualice de forma frecuente para que no genere problemas ni aumente la deuda técnica.
- Tambien se valorara que el peso final de las imagenes sea menor.

## Opciones
Las opciones que se han considerado son:
- [alpine](https://hub.docker.com/_/alpine): Recibe actualizaciones de forma frecuente y tiene un peso muy reducido de 5MB, sin embargo como solo tiene lo mínimo si se usa sería necesario instalar python y el resto de dependencias lo que aumentaria bastante su peso.
- [python](https://hub.docker.com/_/python): Recibe actualizaciones recientes aunque es bastante mas pesado que alpine, sin embargo ya trae instalado python de serie y tiene varias opciones mas ligeras que la base como slim-bullseye o alpine.
- [ubuntu](https://hub.docker.com/_/ubuntu): Recibe actualizaciones de forma regular pero su peso es mayor que alpine y se sigue necesitando instalar python y las dependencias, lo que aumenta su peso.

## Elección
Se han compararado las opciones mencionadas anteriormente con este [resultado](./comparacion.png).
Se ha decidido usar python alpine debido a que no tiene un peso demasiado elevado y ya trae python instalado por defecto, por lo que su peso no aumentara tanto al realizar la instalación.
