from precios_almendra.almendra import Almendra

def test_agregar_precio():
    almendra=Almendra("prueba")
    almendra.agregar_precio("01/01/25",10.95)
    assert(almendra.precios=={"01/01/25":10.95})

def test_obtener_precio():
    almendra=Almendra("prueba")
    almendra.agregar_precio("01/01/25",10.95)
    assert(almendra.obtener_precio("01/01/25")==10.95)
