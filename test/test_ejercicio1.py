import pytest
from ejercicio1 import calcular_precio_entrada

def test_nino_no_estudiante():
    assert calcular_precio_entrada(10, 'no') == 10000.0

def test_nino_estudiante():
    assert calcular_precio_entrada(10, 'si') == 9000.0

def test_adolescente_no_estudiante():
    assert calcular_precio_entrada(15, 'no') == 15000.0

def test_adolescente_estudiante():
    assert calcular_precio_entrada(15, 'si') == 13500.0

def test_adulto_no_estudiante():
    assert calcular_precio_entrada(25, 'no') == 20000.0

def test_adulto_estudiante():
    assert calcular_precio_entrada(25, 'si') == 18000.0

def test_edad_negativa():
    with pytest.raises(ValueError):
        calcular_precio_entrada(-5, 'no')

def test_respuesta_estudiante_invalida():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, 'maybe')

def test_borde_edad_nino_adolescente():
    assert calcular_precio_entrada(12, 'no') == 15000.0

def test_borde_edad_adolescente_adulto():
    assert calcular_precio_entrada(18, 'si') == 18000.0

def test_borde_edad_nino_adolescente_estudiante():
    assert calcular_precio_entrada(12, 'si') == 13500.0

def test_borde_edad_adolescente_adulto_estudiante():
    assert calcular_precio_entrada(18, 'si') == 18000.0

def test_edad_cero_no_estudiante():
    assert calcular_precio_entrada(0, 'no') == 10000.0

def test_edad_cero_estudiante():
    assert calcular_precio_entrada(0, 'si') == 9000.0

def test_edad_muy_alta_no_estudiante():
    assert calcular_precio_entrada(120, 'no') == 20000.0

def test_edad_muy_alta_estudiante():
    assert calcular_precio_entrada(120, 'si') == 18000.0

def test_respuesta_estudiante_mayusculas():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, 'SI')

def test_respuesta_estudiante_con_espacios():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, ' si ')

def test_edad_string():
    with pytest.raises(TypeError):
        calcular_precio_entrada('veinte', 'no')

def test_respuesta_estudiante_numerica():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, 1)

def test_respuesta_estudiante_vacia():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, '')

def test_edad_nulo():
    with pytest.raises(TypeError):
        calcular_precio_entrada(None, 'no')

def test_respuesta_estudiante_nulo():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, None)

def test_respuesta_estudiante_booleano():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, True)

def test_edad_lista():
    with pytest.raises(TypeError):
        calcular_precio_entrada([20], 'no')

def test_respuesta_estudiante_lista():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, ['si'])

def test_edad_diccionario():
    with pytest.raises(TypeError):
        calcular_precio_entrada({'edad': 20}, 'no')

def test_respuesta_estudiante_diccionario():
    with pytest.raises(ValueError):
        calcular_precio_entrada(20, {'estudiante': 'si'})

def test_edad_con_espacios():
    with pytest.raises(TypeError):
        calcular_precio_entrada(' 20 ', 'no')

