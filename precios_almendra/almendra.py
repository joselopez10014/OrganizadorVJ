from datetime import datetime

#Clase Almendra que indica de que tipo es la almendra y cual es su precio segun fecha
class Almendra:
    def __init__(self, tipo):
        self.tipo = tipo
        self.precios = {}  # Diccionario donde las claves son fechas y los valores son los precios.
        
    #Función para agregar un nuevo precio a la almendra, necesita un precio que es un número positivo y una fecha en formato 'AAAA-MM-DD'.No se admiten dos precios con la misma fecha
    def agregar_precio(self, fecha, precio):
        if not self._validar_fecha(fecha):
            raise ValueError(f"La fecha '{fecha}' no es válida. Use el formato 'AAAA-MM-DD'.")
        if precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        if fecha in self.precios:
            raise ValueError(f"Ya existe un precio para la fecha {fecha}.")
        self.precios[fecha] = precio

    #Función que devuelve el precio de la almendra en la fecha indicada
    def obtener_precio(self, fecha):
        return self.precios.get(fecha, None)

    #Función que devuelve todos los precios que ha tenido la almendra con sus fechas
    def listar_precios(self):
        return self.precios.items()
    
    #Función que comprueba el formato de la fecha. Devuelve true si tiene el formato correpto y false si no
    @staticmethod
    def _validar_fecha(fecha):
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False