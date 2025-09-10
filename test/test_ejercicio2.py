import pytest
from ejercicio2 import procesar_comando

def test_procesar_comando_guardar():

    resultado = procesar_comando("guardar")
    assert resultado == "Guardando archivo..."

def test_procesar_comando_cargar():

    resultado = procesar_comando("cargar")
    assert resultado == "Cargando archivo..."

def test_procesar_comando_salir():

    resultado = procesar_comando("salir")
    assert resultado is None

def test_procesar_comando_invalido():

    resultado = procesar_comando("comando_invalido")
    assert resultado == "Error: Comando no válido. Intente nuevamente."

def test_procesar_comando_con_espacios():

    resultado = procesar_comando("  guardar  ")
    assert resultado == "Guardando archivo..."

def test_procesar_comando_mayusculas():

    resultado = procesar_comando("GUARDAR")
    assert resultado == "Guardando archivo..."


def test_procesar_comando_vacio():

    resultado = procesar_comando("")
    assert resultado == "Error: Comando no válido. Intente nuevamente."

def test_procesar_comando_espacios_vacios():

    resultado = procesar_comando("     ")
    assert resultado == "Error: Comando no válido. Intente nuevamente."