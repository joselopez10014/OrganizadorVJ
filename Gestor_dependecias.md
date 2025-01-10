# Gestor de dependencias
## Requisitos
Estos son los criterios que se buscan en el gestor de dependencias:
- Simplicidad: El gestor no debe de ser demasiado complejo para facilitar su comprensión y su uso.
- Fácil de aprender: El proyecto es simple por lo que el gestor debería de ser fácil de aprender y usar para no añadir una dificultad innecesaria al proyecto.
## Opciones
He encontrado varias opciones que se pueden usar como gestor de dependencia en python:
- Poetry: Poetry es una herramienta que te ayuda a declarar, administrar e instalar dependencias de proyectos de Python. Reemplaza setup.py, requirements.txt, setup.cfg, MANIFEST.in y Pipfile con pyproject.toml. Asegura la compatibilidad del proyecto al manejar versiones específicas de las dependencias.
- Uv: UV es un gestor de paquetes y entornos virtuales alternativo para Python, desarrollado en Rust y que nos promete ser muy rápido en los procesos que pretende reemplazar de PIP y VENV. Tiene un gran rendimiento, además es compatible con pyproject.toml. Es muy reciente por lo que aun puede ser difícil encontrar documentación.
- Conda: Conda es una herramienta de gestión de paquetes y entornos proporcionada por Anaconda. Puedes usar conda para crear un nuevo entorno virtual y luego agregar/administrar sus dependencias. Es mas complejo de usar y no esta enfocado a python.
## Elección
Conda es mas complejo de usar que las otras opciones por lo que lo descarto. Entre Uv y Poetry he escogido poetry debido a que Uv es mas nuevo por lo que tiene menos documentación y puede ser mas difícil encontrar soluciones a problemas.