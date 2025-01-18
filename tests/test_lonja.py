from lonja import Lonja
from almendra import Almendra
from unittest.mock import patch, Mock


def test_extraer_datos():
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

        lonjafalsa = Lonja("prueba")

        lonjafalsa.extraer_datos("http://example.com")

    almendra_a = lonjafalsa.obtener_almendra("Tipo A")
    almendra_b = lonjafalsa.obtener_almendra("Tipo B")

    assert(almendra_a.precios == {"01/01/23": 10.5} and almendra_b.precios == {"01/01/23": 20.7, "02/01/23": 30.2})

def test_agregar_almendra():
    lonja = Lonja("prueba")
    lonja.agregar_almendra(Almendra("Tipo A"))
    assert(lonja.almendras[0].tipo=="Tipo A")

def test_obtener_almendra():
    lonja = Lonja("prueba")
    almendra=Almendra("Tipo A")
    lonja.agregar_almendra(almendra)
    lonja.agregar_almendra(Almendra("Tipo b"))
    assert(almendra==lonja.obtener_almendra("Tipo A"))
