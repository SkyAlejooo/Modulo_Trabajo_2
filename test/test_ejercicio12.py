import pytest
from ejercicio12 import simular_lanzamientos


def test_simular_lanzamientos_tipo_retorno():
    resultado = simular_lanzamientos(100)
    assert isinstance(resultado, dict)


def test_simular_lanzamientos_rango_sumas():

    resultado = simular_lanzamientos(1000)


    for suma in resultado.keys():
        assert 2 <= suma <= 12


def test_simular_lanzamientos_cantidad_correcta():

    cantidad = 500
    resultado = simular_lanzamientos(cantidad)

    total_lanzamientos = sum(resultado.values())
    assert total_lanzamientos == cantidad


def test_simular_lanzamientos_valores_positivos():

    resultado = simular_lanzamientos(100)

    for frecuencia in resultado.values():
        assert frecuencia >= 0


def test_simular_lanzamientos_todas_sumas_posibles():

    resultado = simular_lanzamientos(10000)


    for suma in range(2, 13):
        assert suma in resultado
        assert resultado[suma] > 0


def test_simular_lanzamientos_diferentes_cantidades():

    for cantidad in [10, 100, 1000, 5000]:
        resultado = simular_lanzamientos(cantidad)
        total = sum(resultado.values())
        assert total == cantidad


def test_simular_lanzamientos_distribucion_aproximada():

    resultado = simular_lanzamientos(10000)


    assert resultado[7] > resultado[2]
    assert resultado[7] > resultado[12]
    assert resultado[6] > resultado[2]
    assert resultado[8] > resultado[12]


def test_simular_lanzamientos_estructura():

    resultado = simular_lanzamientos(100)


    for clave in resultado.keys():
        assert isinstance(clave, int)


    for valor in resultado.values():
        assert isinstance(valor, int)


def test_simular_lanzamientos_cero_lanzamientos():

    resultado = simular_lanzamientos(0)
    assert resultado == {}
    assert len(resultado) == 0


def test_simular_lanzamientos_un_lanzamiento():

    resultado = simular_lanzamientos(1)
    assert len(resultado) == 1
    total = sum(resultado.values())
    assert total == 1


    suma = list(resultado.keys())[0]
    assert 2 <= suma <= 12


def test_simular_lanzamientos_consistencia():

    resultados = []
    for _ in range(5):
        resultado = simular_lanzamientos(1000)
        resultados.append(resultado)


    for resultado in resultados:
        total = sum(resultado.values())
        assert total == 1000


    for resultado in resultados:
        for suma in resultado.keys():
            assert 2 <= suma <= 12


def test_simular_lanzamientos_probabilidades_relativas():

    resultado = simular_lanzamientos(10000)


    suma_mas_frecuente = max(resultado, key=resultado.get)
    assert suma_mas_frecuente == 7


    assert resultado[2] < resultado[6]
    assert resultado[2] < resultado[7]
    assert resultado[2] < resultado[8]
    assert resultado[12] < resultado[6]
    assert resultado[12] < resultado[7]
    assert resultado[12] < resultado[8]


def test_simular_lanzamientos_suma_minima_maxima():

    resultado = simular_lanzamientos(1000)


    sumas_presentes = set(resultado.keys())
    assert sumas_presentes.issubset(set(range(2, 13)))


def test_simular_lanzamientos_frecuencia_acumulada():

    resultado = simular_lanzamientos(500)

    total_frecuencia = sum(resultado.values())
    assert total_frecuencia == 500


def test_simular_lanzamientos_valores_razonables():

    resultado = simular_lanzamientos(10000)

    for suma in range(2, 13):
        assert resultado[suma] > 0


    assert 1300 <= resultado[7] <= 2000



def verificar_distribucion(resultado, cantidad_lanzamientos):

    total = sum(resultado.values())
    assert total == cantidad_lanzamientos

    for suma in range(2, 13):
        if suma in resultado:
            assert resultado[suma] >= 0
            assert 2 <= suma <= 12


def test_con_funcion_helper():

    cantidades = [100, 1000, 5000]

    for cantidad in cantidades:
        resultado = simular_lanzamientos(cantidad)
        verificar_distribucion(resultado, cantidad)


def test_simular_lanzamientos_orden_claves():

    resultado = simular_lanzamientos(100)

    for clave in resultado.keys():
        assert isinstance(clave, int)
        assert 2 <= clave <= 12


def test_simular_lanzamientos_sin_valores_negativos():

    resultado = simular_lanzamientos(100)

    for frecuencia in resultado.values():
        assert frecuencia >= 0