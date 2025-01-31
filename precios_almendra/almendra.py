from datetime import datetime

class Almendra:
    def __init__(self, tipo):
        self.tipo = tipo
        self.precios = {}  
        
    def agregar_precio(self, fecha, precio):
        if not self._validar_fecha(fecha):
            raise ValueError(f"La fecha '{fecha}' no es válida. Use el formato 'DD-MM-AAAA'.")
        if precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        if fecha in self.precios:
            raise ValueError(f"Ya existe un precio para la fecha {fecha}.")
        self.precios[fecha] = precio

    def obtener_precio(self, fecha):
        return self.precios.get(fecha, None)

    def listar_precios(self):
        return self.precios.items()
    
    @staticmethod
    def _validar_fecha(fecha):
        try:
            datetime.strptime(fecha, "%d/%m/%y")
            return True
        except ValueError:
            return False
