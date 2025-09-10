import pytest
from unittest.mock import patch, MagicMock
from ejercicio5 import clasificar_numero, main

def test_clasificar_numero_par_no_multiplo_5():
    resultado = clasificar_numero(4)
    assert resultado == ("Par", "")

def test_clasificar_numero_impar_no_multiplo_5():
    resultado = clasificar_numero(7)
    assert resultado == ("Impar", "")

def test_clasificar_numero_par_multiplo_5():
    resultado = clasificar_numero(10)
    assert resultado == ("Par", "y también es múltiplo de 5")

def test_clasificar_numero_impar_multiplo_5():
    resultado = clasificar_numero(15)
    assert resultado == ("Impar", "y también es múltiplo de 5")

def test_clasificar_numero_cero():
    resultado = clasificar_numero(0)
    assert resultado == ("Par", "y también es múltiplo de 5")

def test_clasificar_numero_negativo_par():
    resultado = clasificar_numero(-4)
    assert resultado == ("Par", "")

def test_clasificar_numero_negativo_impar():
    resultado = clasificar_numero(-7)
    assert resultado == ("Impar", "")

def test_clasificar_numero_negativo_multiplo_5():
    resultado = clasificar_numero(-10)
    assert resultado == ("Par", "y también es múltiplo de 5")

@patch('builtins.input')
@patch('builtins.print')
def test_main_numero_par_no_multiplo_5(mock_print, mock_input):
    mock_input.return_value = '4'

    main()

    mock_input.assert_called_once_with("Ingrese un número: ")
    mock_print.assert_called_once_with("El número 4 es Par")


@patch('builtins.input')
@patch('builtins.print')
def test_main_numero_par_multiplo_5(mock_print, mock_input):
    mock_input.return_value = '10'
    main()
    mock_print.assert_called_once_with("El número 10 es Par y también es múltiplo de 5")

@patch('builtins.input')
@patch('builtins.print')
def test_main_numero_impar_no_multiplo_5(mock_print, mock_input):
    mock_input.return_value = '7'
    main()
    mock_print.assert_called_once_with("El número 7 es Impar")


@patch('builtins.input')
@patch('builtins.print')
def test_main_numero_impar_multiplo_5(mock_print, mock_input):
    mock_input.return_value = '15'
    main()
    mock_print.assert_called_once_with("El número 15 es Impar y también es múltiplo de 5")


@patch('builtins.input')
@patch('builtins.print')
def test_main_entrada_invalida(mock_print, mock_input):
    mock_input.return_value = 'no_es_un_numero'
    main()
    mock_print.assert_called_once_with("Error: Debe ingresar un número válido.")


@patch('builtins.input')
@patch('builtins.print')
def test_main_numero_cero(mock_print, mock_input):
    mock_input.return_value = '0'
    main()
    mock_print.assert_called_once_with("El número 0 es Par y también es múltiplo de 5")


@patch('builtins.input')
@patch('builtins.print')
def test_main_numero_negativo(mock_print, mock_input):
    mock_input.return_value = '-12'
    main()
    mock_print.assert_called_once_with("El número -12 es Par")


@patch('builtins.input')
@patch('builtins.print')
def test_main_numero_negativo_multiplo_5(mock_print, mock_input):
    mock_input.return_value = '-25'
    main()
    mock_print.assert_called_once_with("El número -25 es Impar y también es múltiplo de 5")

def test_formato_mensaje():
    test_cases = [
        (4, "El número 4 es Par"),
        (10, "El número 10 es Par y también es múltiplo de 5"),
        (7, "El número 7 es Impar"),
        (15, "El número 15 es Impar y también es múltiplo de 5"),
        (0, "El número 0 es Par y también es múltiplo de 5")
    ]

    for numero, mensaje_esperado in test_cases:
        paridad, mensaje_extra = clasificar_numero(numero)

        resultado = f"El número {numero} es {paridad}"
        if mensaje_extra:
            resultado += f" {mensaje_extra}"

        assert resultado == mensaje_esperado


if __name__ == "__main__":
    pytest.main([__file__, "-v"])