help:
	@echo "Comandos disponibles:"
	@echo "  install        		Instala el gestor de dependencias Poetry"
	@echo "  check        			Realiza las comprobaciones"
	@echo "  test        			Realiza los test"

install:
	@echo "Se va a instalar poetry"
	@curl -sSL https://install.python-poetry.org | python3 -


check:
	@echo "Comprobando..."
	@for file in precios_almendra/*.py; do \
		echo "Ejecutando $$file..."; \
		python3 $$file || { echo "Error en $$file"; exit 1; }; \
	done
	@echo "Todo funciona correctamente."

test:
	poetry run pytest -v
