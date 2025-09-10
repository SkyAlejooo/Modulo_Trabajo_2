import pytest
from ejercicio11 import validar_cedula


def test_validar_cedula_valida_suma_par():

    cedulas_validas = ["22", "1234", "1111", "2468", "3579", "123"]  # 123: 1+2+3=6 (par)

    for cedula in cedulas_validas:
        resultado = validar_cedula(cedula)
        assert resultado == True


def test_validar_cedula_invalida_suma_impar():

    cedulas_invalidas = ["1", "111", "135", "24681"]

    for cedula in cedulas_invalidas:
        resultado = validar_cedula(cedula)
        assert resultado == False


def test_validar_cedula_con_caracteres_no_numericos():

    cedulas_invalidas = ["12a3", "abc", "12-34", "12.34", "123 "]

    for cedula in cedulas_invalidas:
        resultado = validar_cedula(cedula)
        assert resultado == False


def test_validar_cedula_vacia():

    resultado = validar_cedula("")
    assert resultado == False


def test_validar_cedula_ceros():

    resultado1 = validar_cedula("0000")
    resultado2 = validar_cedula("00")

    assert resultado1 == True
    assert resultado2 == True


def test_validar_cedula_larga():

    resultado1 = validar_cedula("1234567890")
    assert resultado1 == False


    resultado2 = validar_cedula("1234567891")
    assert resultado2 == True


def test_validar_cedula_un_digito():

    assert validar_cedula("0") == True
    assert validar_cedula("2") == True
    assert validar_cedula("4") == True
    assert validar_cedula("6") == True
    assert validar_cedula("8") == True

    # Dígitos impares → False
    assert validar_cedula("1") == False
    assert validar_cedula("3") == False
    assert validar_cedula("5") == False
    assert validar_cedula("7") == False
    assert validar_cedula("9") == False


def test_validar_cedula_numeros_grandes():
    assert validar_cedula("9999") == True


    assert validar_cedula("9998") == False


def test_validar_cedula_espacios():

    assert validar_cedula(" 123") == False
    assert validar_cedula("123 ") == False
    assert validar_cedula("12 3") == False



def crear_casos_prueba():

    return {
        'validos': ["0", "00", "11", "22", "123", "1234", "2468", "3579"],
        'invalidos': ["1", "3", "5", "111", "135", "24681"],
        'no_numericos': ["abc", "12a", "1.2", "1-2", "12 "]
    }


def test_con_funcion_helper():

    casos = crear_casos_prueba()


    for cedula in casos['validos']:
        resultado = validar_cedula(cedula)
        assert resultado == True, f"La cédula {cedula} debería ser válida"


    for cedula in casos['invalidos']:
        resultado = validar_cedula(cedula)
        assert resultado == False, f"La cédula {cedula} debería ser inválida"


    for cedula in casos['no_numericos']:
        resultado = validar_cedula(cedula)
        assert resultado == False, f"La cédula {cedula} debería ser inválida"