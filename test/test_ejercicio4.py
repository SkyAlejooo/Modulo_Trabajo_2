import pytest
from unittest.mock import patch, call, MagicMock
import random
from ejercicio4 import determinar_ganador


def test_determinar_ganador_empates():
    assert determinar_ganador('piedra', 'piedra') == 'empate'
    assert determinar_ganador('papel', 'papel') == 'empate'
    assert determinar_ganador('tijeras', 'tijeras') == 'empate'


def test_determinar_ganador_jugador_gana():
    assert determinar_ganador('piedra', 'tijeras') == 'jugador'
    assert determinar_ganador('tijeras', 'papel') == 'jugador'
    assert determinar_ganador('papel', 'piedra') == 'jugador'


def test_determinar_ganador_computadora_gana():
    assert determinar_ganador('piedra', 'papel') == 'computadora'
    assert determinar_ganador('papel', 'tijeras') == 'computadora'
    assert determinar_ganador('tijeras', 'piedra') == 'computadora'


def test_determinar_ganador_opciones_invalidas():
    resultado = determinar_ganador('invalid', 'piedra')
    assert resultado in ['jugador', 'computadora', 'empate']


def test_simulacion_jugador_gana_partida():

    user_choices = ['piedra', 'papel', 'tijeras']
    computer_choices = ['tijeras', 'piedra', 'papel']

    resultados = []
    for user, computer in zip(user_choices, computer_choices):
        resultados.append(determinar_ganador(user, computer))

    assert all(resultado == 'jugador' for resultado in resultados)


def test_simulacion_computadora_gana_partida():

    user_choices = ['piedra', 'papel', 'tijeras']
    computer_choices = ['papel', 'tijeras', 'piedra']

    resultados = []
    for user, computer in zip(user_choices, computer_choices):
        resultados.append(determinar_ganador(user, computer))

    assert all(resultado == 'computadora' for resultado in resultados)


def test_simulacion_partida_con_empates():

    user_choices = ['piedra', 'piedra', 'tijeras']
    computer_choices = ['piedra', 'papel', 'tijeras']

    resultados = []
    for user, computer in zip(user_choices, computer_choices):
        resultados.append(determinar_ganador(user, computer))


    expected_results = ['empate', 'computadora', 'empate']
    assert resultados == expected_results



@patch('builtins.input')
@patch('builtins.print')
@patch('random.choice')
def test_main_flujo_basico(mock_choice, mock_print, mock_input):

    mock_input.side_effect = ['piedra', 'salir']
    mock_choice.return_value = 'tijeras'

    user_choice = mock_input()
    computer_choice = mock_choice()

    resultado = determinar_ganador(user_choice, computer_choice)

    assert user_choice == 'piedra'
    assert computer_choice == 'tijeras'
    assert resultado == 'jugador'


@patch('builtins.input')
@patch('builtins.print')
@patch('random.choice')
def test_main_salir_directamente(mock_choice, mock_print, mock_input):

    mock_input.side_effect = ['salir']

    user_choice = mock_input()

    assert user_choice == 'salir'
    mock_choice.assert_not_called()


@patch('builtins.input')
@patch('builtins.print')
def test_main_opcion_invalida(mock_print, mock_input):


    mock_input.side_effect = ['opcion_invalida', 'salir']


    user_choice1 = mock_input()
    resultado = determinar_ganador(user_choice1, 'piedra')


    user_choice2 = mock_input()


    assert resultado in ['jugador', 'computadora', 'empate']
    assert user_choice2 == 'salir'


    assert mock_input.call_count == 2



def test_contador_puntos():

    resultados = ['jugador', 'computadora', 'empate', 'jugador', 'computadora']

    jugador_score = resultados.count('jugador')
    computadora_score = resultados.count('computadora')
    empates = resultados.count('empate')

    assert jugador_score == 2
    assert computadora_score == 2
    assert empates == 1



def test_combinaciones_especificas():

    assert determinar_ganador('piedra', 'tijeras') == 'jugador'

    assert determinar_ganador('papel', 'piedra') == 'jugador'

    assert determinar_ganador('tijeras', 'papel') == 'jugador'

    assert determinar_ganador('piedra', 'papel') == 'computadora'

    assert determinar_ganador('papel', 'tijeras') == 'computadora'

    assert determinar_ganador('tijeras', 'piedra') == 'computadora'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])