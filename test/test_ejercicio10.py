import pytest
from ejercicio10 import transponer_matriz_bucles, transponer_matriz_comprehension, main


def test_transponer_bucles_matriz_2x3():

    matriz_original = [[1, 2, 3], [4, 5, 6]]
    resultado_esperado = [[1, 4], [2, 5], [3, 6]]

    resultado = transponer_matriz_bucles(matriz_original)

    assert resultado == resultado_esperado


def test_transponer_bucles_matriz_3x2():

    matriz_original = [[1, 2], [3, 4], [5, 6]]
    resultado_esperado = [[1, 3, 5], [2, 4, 6]]

    resultado = transponer_matriz_bucles(matriz_original)

    assert resultado == resultado_esperado


def test_transponer_bucles_matriz_1x1():

    matriz_original = [[5]]
    resultado_esperado = [[5]]

    resultado = transponer_matriz_bucles(matriz_original)

    assert resultado == resultado_esperado


def test_transponer_bucles_matriz_vacia():

    matriz_original = []
    resultado_esperado = []

    resultado = transponer_matriz_bucles(matriz_original)

    assert resultado == resultado_esperado



def test_transponer_comprehension_matriz_2x3():

    matriz_original = [[1, 2, 3], [4, 5, 6]]
    resultado_esperado = [[1, 4], [2, 5], [3, 6]]

    resultado = transponer_matriz_comprehension(matriz_original)

    assert resultado == resultado_esperado


def test_transponer_comprehension_matriz_3x2():

    matriz_original = [[1, 2], [3, 4], [5, 6]]
    resultado_esperado = [[1, 3, 5], [2, 4, 6]]

    resultado = transponer_matriz_comprehension(matriz_original)

    assert resultado == resultado_esperado


def test_transponer_comprehension_matriz_1x1():

    matriz_original = [[5]]
    resultado_esperado = [[5]]

    resultado = transponer_matriz_comprehension(matriz_original)

    assert resultado == resultado_esperado


def test_transponer_comprehension_matriz_vacia():

    matriz_original = []
    resultado_esperado = []

    resultado = transponer_matriz_comprehension(matriz_original)

    assert resultado == resultado_esperado



def test_ambos_metodos_igual_resultado():

    matrices_prueba = [
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2], [3, 4], [5, 6]],
        [[1]],
        [[1, 2], [3, 4]]
    ]

    for matriz in matrices_prueba:
        resultado_bucles = transponer_matriz_bucles(matriz)
        resultado_comprehension = transponer_matriz_comprehension(matriz)

        assert resultado_bucles == resultado_comprehension



def test_main_muestra_resultados_correctos(capsys):
    main()

    captured = capsys.readouterr()
    output = captured.out


    assert "Matriz original:" in output
    assert "Transpuesta (bucles):" in output
    assert "Transpuesta (comprehension):" in output


    assert "[1, 2, 3]" in output
    assert "[4, 5, 6]" in output
    assert "[1, 4]" in output
    assert "[2, 5]" in output
    assert "[3, 6]" in output


def test_matriz_con_strings():

    matriz_original = [["a", "b"], ["c", "d"]]
    resultado_esperado = [["a", "c"], ["b", "d"]]

    resultado_bucles = transponer_matriz_bucles(matriz_original)
    resultado_comprehension = transponer_matriz_comprehension(matriz_original)

    assert resultado_bucles == resultado_esperado
    assert resultado_comprehension == resultado_esperado


def test_matriz_con_floats():

    matriz_original = [[1.5, 2.5], [3.5, 4.5]]
    resultado_esperado = [[1.5, 3.5], [2.5, 4.5]]

    resultado_bucles = transponer_matriz_bucles(matriz_original)
    resultado_comprehension = transponer_matriz_comprehension(matriz_original)

    assert resultado_bucles == resultado_esperado
    assert resultado_comprehension == resultado_esperado