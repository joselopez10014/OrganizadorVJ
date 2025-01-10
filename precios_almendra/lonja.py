from almendra import Almendra

#Clase Lonja que indica el nombre del punto de venta y guarda todos los tipos del almendra que se pueden vender aqui
class Lonja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.almendras = []
    
    #Función que añade un nuevo tipo de almendra a la lonja. Necesita que se le pasa un atributo de la clase Almendra que no este ya en la lista
    def agregar_almendra(self, almendra):
        if not isinstance(almendra, Almendra):
            raise ValueError("Solo se pueden agregar objetos de tipo Almendra.")
        if almendra in self.almendras:
            raise ValueError(f"La almendra '{almendra.tipo}' ya está en la lonja.")
        self.almendras.append(almendra)

    #Función que muestra todos los tipos de almendra que hay en la lonja
    def listar_almendras(self):
        return [almendra.tipo for almendra in self.almendras]