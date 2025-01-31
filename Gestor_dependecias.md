# Gestor de dependencias
## Requisitos
Estos son los criterios que se buscan en el gestor de dependencias:
- Mantenimiento: Se busca que tenga actualizaciones frecuentes para evitar que se quede desactualizado y empiece a generar una deuda técnica
- Uso de pyproject.toml: Se valora si se usa este archivo, ya que es el estándar recomendado para gestionar configuraciones de proyectos en Python, propuesto por PEP 518.
- Madurez: Se valoran mas los gestores que llevan mas tiempo activos ya que suelen ser más confiables y estables

## Opciones
He encontrado varias opciones que se pueden usar como gestor de dependencia en python:
- [Poetry](https://github.com/python-poetry/poetry): Reemplaza setup.py, requirements.txt, setup.cfg, MANIFEST.in y Pipfile con pyproject.toml. Asegura la compatibilidad del proyecto al manejar versiones específicas de las dependencias.
- [Uv](https://github.com/astral-sh/uv): Tiene un gran rendimiento, además es compatible con pyproject.toml. Es muy reciente por lo que no es el mas confiable y puede sufrir grandes cambios a lo largo de las actualizaciones.
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html): Conda se puede usar para crear un nuevo entorno virtual y luego agregar/administrar sus dependencias, sin embargo no hace uso del archivo pyproject.toml.

## Elección
Las tres opciones son actualizadas de forma frecuente.Conda, al contrario que Uv y Poetry, no hace uso del archivo pyproject.toml por lo que lo descartamos. Entre Uv y Poetry he escogido Poetry ya que tiene una mayor madurez que Uv que fue creado hace no mucho.
