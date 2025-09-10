import pytest
from ejercicio7 import combinar_listas, main  # Reemplaza 'tu_archivo' con el nombre real



def test_combinar_listas_exitoso():

    nombres = ["Ana", "Luis", "Maria"]
    notas = [4.5, 3.8, 4.9]
    resultado_esperado = {"Ana": 4.5, "Luis": 3.8, "Maria": 4.9}

    resultado = combinar_listas(nombres, notas)


    assert resultado == resultado_esperado
    assert len(resultado) == 3
    assert "Ana" in resultado
    assert resultado["Luis"] == 3.8


def test_combinar_listas_vacias():

    nombres = []
    notas = []
    resultado_esperado = {}


    resultado = combinar_listas(nombres, notas)


    assert resultado == resultado_esperado
    assert len(resultado) == 0


def test_combinar_listas_longitud_diferente():

    nombres = ["Ana", "Luis"]
    notas = [4.5]


    with pytest.raises(ValueError) as error_info:
        combinar_listas(nombres, notas)


    assert str(error_info.value) == "Las listas deben tener la misma longitud"


def test_combinar_listas_un_elemento():

    nombres = ["Ana"]
    notas = [4.5]
    resultado_esperado = {"Ana": 4.5}


    resultado = combinar_listas(nombres, notas)


    assert resultado == resultado_esperado
    assert len(resultado) == 1


def test_combinar_listas_con_duplicados():

    nombres = ["Ana", "Ana", "Luis"]
    notas = [4.5, 3.8, 4.9]
    resultado_esperado = {"Ana": 3.8, "Luis": 4.9}


    resultado = combinar_listas(nombres, notas)


    assert resultado == resultado_esperado
    assert resultado["Ana"] == 3.8



def test_combinar_listas_con_none():

    nombres = [None, "Luis"]
    notas = [4.5, 3.8]
    resultado_esperado = {None: 4.5, "Luis": 3.8}


    resultado = combinar_listas(nombres, notas)


    assert resultado == resultado_esperado
    assert None in resultado


def test_combinar_listas_con_notas_negativas():

    nombres = ["Ana", "Luis"]
    notas = [-1.0, 5.0]
    resultado_esperado = {"Ana": -1.0, "Luis": 5.0}


    resultado = combinar_listas(nombres, notas)


    assert resultado == resultado_esperado


def test_combinar_listas_con_notas_cero():

    nombres = ["Ana"]
    notas = [0.0]
    resultado_esperado = {"Ana": 0.0}


    resultado = combinar_listas(nombres, notas)


    assert resultado == resultado_esperado


def test_main_funciona_correctamente(capsys):

    main()


    captured = capsys.readouterr()
    output = captured.out

    assert "Reporte de notas:" in output
    assert "El estudiante Ana tiene una nota de 4.5" in output
    assert "El estudiante Luis tiene una nota de 3.8" in output
    assert "El estudiante Maria tiene una nota de 4.9" in output
    assert "El estudiante Carlos tiene una nota de 3.2" in output
    assert "El estudiante Laura tiene una nota de 4.7" in output
    assert "Error:" not in output



def crear_datos_prueba():

    return {
        "nombres": ["Juan", "Pedro"],
        "notas": [4.0, 3.5],
        "esperado": {"Juan": 4.0, "Pedro": 3.5}
    }



def test_combinar_con_helper():

    datos = crear_datos_prueba()
    resultado = combinar_listas(datos["nombres"], datos["notas"])
    assert resultado == datos["esperado"]



def test_combinar_listas_tipos_correctos():

    nombres = ["Ana", "Luis"]
    notas = [4.5, 3.8]

    resultado = combinar_listas(nombres, notas)


    assert isinstance(resultado, dict)


    for nombre in resultado.keys():
        assert isinstance(nombre, str)


    for nota in resultado.values():
        assert isinstance(nota, (int, float))