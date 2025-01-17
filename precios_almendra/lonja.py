from almendra import Almendra
import requests
from datetime import datetime
from bs4 import BeautifulSoup as b

class Lonja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.almendras = []
    
    def agregar_almendra(self, almendra):
        if not isinstance(almendra, Almendra):
            raise ValueError("Solo se pueden agregar objetos de tipo Almendra.")
        if almendra in self.almendras:
            raise ValueError(f"La almendra '{almendra.tipo}' ya está en la lonja.")
        self.almendras.append(almendra)

    def listar_almendras(self):
        return [almendra.tipo for almendra in self.almendras]
    
    def obtener_almendra(self, tipo):
        resultado=None
        for almendra in self.almendras:
            if tipo in almendra.tipo==tipo:
                resultado=almendra
        return resultado
    
    def extraer_datos(self,url):
        html=requests.get(url)
        contenido=html.content
        soup=b(contenido,"html.parser")
        tabla= soup.find("div",class_="supsystic-tables-wrap")
        headers= tabla.find("thead").find_all("th")
    
        tipos_almendra=[]
        almendras={}
        
        for th in headers[1:]: 
            tipo= th.get_text(strip=True)
            tipos_almendra.append(tipo)
            almendras[tipo]=Almendra(tipo)
        
        filas= tabla.find("tbody").find_all("tr")
        for fila in filas:
            celdas= fila.find_all("td")
            fecha= celdas[0].get_text(strip=True)
            try:
                datetime.strptime(fecha, "%d/%m/%y")
                for i, celda in enumerate(celdas[1:]):
                    precio_str=celda.get_text(strip=True)
                    if precio_str not in ["s/o", "s/c", "-", "s/a"]:
                        precio= float(precio_str.replace(",", "."))
                        tipo= tipos_almendra[i]
                        almendras[tipo].agregar_precio(fecha,precio)
            
            except ValueError:
                print(f"Fecha con formato erroneo se ignora: {fecha}")
            continue 
        for tipo in almendras:
            self.agregar_almendra(almendras[tipo])
