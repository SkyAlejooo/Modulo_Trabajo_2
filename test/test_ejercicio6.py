import pytest
from unittest.mock import patch, call
from ejercicio6 import encontrar_indices, main



def test_encontrar_indices_letra_presente():

    resultado = encontrar_indices("hola mundo", "o")
    assert resultado == [1, 9]  # 'o' en posiciones 1 y 7


def test_encontrar_indices_letra_no_presente():

    resultado = encontrar_indices("hola mundo", "z")
    assert resultado == []


def test_encontrar_indices_case_insensitive_mayuscula():

    resultado = encontrar_indices("Hola Mundo", "h")
    assert resultado == [0]  # 'H' en posición 0


def test_encontrar_indices_case_insensitive_minuscula():

    resultado = encontrar_indices("Hola Mundo", "H")
    assert resultado == [0]  # 'H' en posición 0


def test_encontrar_indices_multiple_occurrences():

    resultado = encontrar_indices("programacion python", "p")
    assert resultado == [0, 13]  # 'p' en posiciones 0 y 13


def test_encontrar_indices_vacio():

    resultado = encontrar_indices("", "a")
    assert resultado == []


def test_encontrar_indices_espacios():

    resultado = encontrar_indices("   ", " ")
    assert resultado == [0, 1, 2]  # 3 espacios


def test_encontrar_indices_caracteres_especiales():

    resultado = encontrar_indices("¡hola!", "!")

    assert resultado == [5]


def test_encontrar_indices_numeros():

    resultado = encontrar_indices("abc123abc", "1")
    assert resultado == [3]  # '1' en posición 3



@patch('builtins.input')
@patch('builtins.print')
def test_main_letra_encontrada(mock_print, mock_input):

    mock_input.side_effect = ["hola mundo", "o"]

    main()


    mock_print.assert_called_once_with("La letra 'o' aparece en las posiciones: [1, 9]")


@patch('builtins.input')
@patch('builtins.print')
def test_main_letra_no_encontrada(mock_print, mock_input):

    mock_input.side_effect = ["hola mundo", "z"]

    main()

    mock_print.assert_called_once_with("La letra 'z' aparece en las posiciones: []")


@patch('builtins.input')
@patch('builtins.print')
def test_main_case_insensitive(mock_print, mock_input):

    mock_input.side_effect = ["Python", "p"]

    main()

    mock_print.assert_called_once_with("La letra 'p' aparece en las posiciones: [0]")


@patch('builtins.input')
@patch('builtins.print')
def test_main_frase_vacia(mock_print, mock_input):

    mock_input.side_effect = ["", "a"]

    main()

    mock_print.assert_called_once_with("La letra 'a' aparece en las posiciones: []")


@patch('builtins.input')
@patch('builtins.print')
def test_main_letra_espacio(mock_print, mock_input):

    mock_input.side_effect = ["hola mundo", " "]

    main()

    mock_print.assert_called_once_with("La letra ' ' aparece en las posiciones: [4]")


@patch('builtins.input')
@patch('builtins.print')
def test_main_multiple_palabras(mock_print, mock_input):

    mock_input.side_effect = ["python es genial", "e"]

    main()

    mock_print.assert_called_once_with("La letra 'e' aparece en las posiciones: [7, 11]")


def test_encontrar_indices_acentos():

    resultado = encontrar_indices("café", "é")
    assert resultado == [3]


def test_encontrar_indices_todos_iguales():

    resultado = encontrar_indices("aaaaa", "a")
    assert resultado == [0, 1, 2, 3, 4]


def test_encontrar_indices_primera_ultima():

    resultado = encontrar_indices("python", "p")
    assert resultado == [0]

    resultado = encontrar_indices("python", "n")
    assert resultado == [5]


@patch('builtins.input')
@patch('builtins.print')
def test_main_orden_llamadas(mock_print, mock_input):

    mock_input.side_effect = ["frase de prueba", "a"]

    main()


    expected_calls = [
        call("Ingrese una frase: "),
        call("Ingrese la letra a buscar: ")
    ]
    mock_input.assert_has_calls(expected_calls)


if __name__ == "__main__":

    print("Ejecutando tests básicos...")


    test_encontrar_indices_letra_presente()
    test_encontrar_indices_caracteres_especiales()
    test_encontrar_indices_multiple_occurrences()
    test_main_multiple_palabras()

    print("✅ Todos los tests básicos pasaron!")

    pytest.main([__file__, "-v"])