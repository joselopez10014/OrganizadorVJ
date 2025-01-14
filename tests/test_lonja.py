from precios_almendra.lonja import Lonja
from bs4 import BeautifulSoup as b
from precios_almendra.almendra import Almendra
from unittest.mock import patch, Mock


def test_extraer_datos():
    # Simula una respuesta de requests.get
    html_prueba = """
    <div class="supsystic-tables-wrap">
        <table>
            <thead>
                <tr>
                    <th>Fecha</th>
                    <th>Tipo A</th>
                    <th>Tipo B</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>01/01/23</td>
                    <td>10,5</td>
                    <td>20,7</td>
                </tr>
                <tr>
                    <td>02/01/23</td>
                    <td>s/o</td>
                    <td>30,2</td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.content = html_prueba
        mock_get.return_value = mock_response

        # Instancia de la clase que contiene extraer_datos
        lonjafalsa = Lonja("prueba")

        # Llama a la función que deseas probar
        lonjafalsa.extraer_datos("http://example.com")

    # Verifica que los datos fueron procesados correctamente
    almendra_a = lonjafalsa.obtener_almendra("Tipo A")
    almendra_b = lonjafalsa.obtener_almendra("Tipo B")

    # Verifica los precios y las fechas procesadas
    assert(almendra_a.precios == {"01/01/23": 10.5} and almendra_b.precios == {"01/01/23": 20.7, "02/01/23": 30.2})
