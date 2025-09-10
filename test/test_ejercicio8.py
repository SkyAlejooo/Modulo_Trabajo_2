import pytest
from ejercicio8 import main


def test_main_procesa_lista_correctamente(capsys):
    main()


    captured = capsys.readouterr()
    output = captured.out


    assert "Lista original de números: [-5, 10, -15, 20, -25, 30]" in output
    assert "Números positivos filtrados: [10, 20, 30]" in output
    assert "Cuadrados de cada número: [25, 100, 225, 400, 625, 900]" in output
    assert "Clasificación de números: ['negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo']" in output


def test_main_contiene_todas_secciones(capsys):
    main()


    captured = capsys.readouterr()
    output = captured.out


    assert "Lista original de números:" in output
    assert "Números positivos filtrados:" in output
    assert "Cuadrados de cada número:" in output
    assert "Clasificación de números:" in output


def test_filtrar_numeros_positivos():

    lista_numeros = [-5, 10, -15, 20, -25, 30]


    numeros_positivos = [numero for numero in lista_numeros if numero > 0]


    assert numeros_positivos == [10, 20, 30]
    assert len(numeros_positivos) == 3
    assert all(numero > 0 for numero in numeros_positivos)


def test_calcular_cuadrados():

    lista_numeros = [-5, 10, -15, 20, -25, 30]


    cuadrados_numeros = [numero ** 2 for numero in lista_numeros]


    assert cuadrados_numeros == [25, 100, 225, 400, 625, 900]
    assert len(cuadrados_numeros) == 6
    assert all(cuadrado >= 0 for cuadrado in cuadrados_numeros)  # Todos deben ser positivos


def test_clasificar_numeros():

    lista_numeros = [-5, 10, -15, 20, -25, 30]


    clasificacion_numeros = ["positivo" if numero >= 0 else "negativo" for numero in lista_numeros]


    expected = ['negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo']
    assert clasificacion_numeros == expected
    assert len(clasificacion_numeros) == 6
    assert clasificacion_numeros.count('positivo') == 3
    assert clasificacion_numeros.count('negativo') == 3


def test_casos_especiales_clasificacion():

    lista_con_cero = [-1, 0, 1]
    clasificacion = ["positivo" if numero >= 0 else "negativo" for numero in lista_con_cero]

    assert clasificacion == ['negativo', 'positivo', 'positivo']


def test_lista_vacia():

    lista_vacia = []


    positivos = [numero for numero in lista_vacia if numero > 0]
    cuadrados = [numero ** 2 for numero in lista_vacia]
    clasificacion = ["positivo" if numero >= 0 else "negativo" for numero in lista_vacia]

    assert positivos == []
    assert cuadrados == []
    assert clasificacion == []


def test_lista_solo_positivos():

    lista_positivos = [1, 2, 3, 4, 5]

    positivos = [numero for numero in lista_positivos if numero > 0]
    cuadrados = [numero ** 2 for numero in lista_positivos]
    clasificacion = ["positivo" if numero >= 0 else "negativo" for numero in lista_positivos]

    assert positivos == [1, 2, 3, 4, 5]
    assert cuadrados == [1, 4, 9, 16, 25]
    assert clasificacion == ['positivo', 'positivo', 'positivo', 'positivo', 'positivo']


def test_lista_solo_negativos():

    lista_negativos = [-1, -2, -3, -4, -5]

    positivos = [numero for numero in lista_negativos if numero > 0]
    cuadrados = [numero ** 2 for numero in lista_negativos]
    clasificacion = ["positivo" if numero >= 0 else "negativo" for numero in lista_negativos]

    assert positivos == []
    assert cuadrados == [1, 4, 9, 16, 25]
    assert clasificacion == ['negativo', 'negativo', 'negativo', 'negativo', 'negativo']



def crear_lista_prueba():

    return {
        'lista': [-2, 4, -6, 8],
        'positivos_esperados': [4, 8],
        'cuadrados_esperados': [4, 16, 36, 64],
        'clasificacion_esperada': ['negativo', 'positivo', 'negativo', 'positivo']
    }


def test_con_funcion_helper():

    datos = crear_lista_prueba()


    positivos = [numero for numero in datos['lista'] if numero > 0]
    cuadrados = [numero ** 2 for numero in datos['lista']]
    clasificacion = ["positivo" if numero >= 0 else "negativo" for numero in datos['lista']]

    assert positivos == datos['positivos_esperados']
    assert cuadrados == datos['cuadrados_esperados']
    assert clasificacion == datos['clasificacion_esperada']