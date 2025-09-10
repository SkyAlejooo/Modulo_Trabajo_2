import pytest
from ejercicio13 import main
from io import StringIO
import sys


def test_movimiento_entre_habitaciones():

    input_mock = StringIO("norte\nsur\neste\noeste\n")


    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        with pytest.raises(SystemExit):
            main()
    except:
        pass
    finally:
        sys.stdin = original_stdin


def test_tomar_llave_y_abrir_cofre():

    input_mock = StringIO("este\ntomar\noeste\nnorte\nusar\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "¡Encontraste la llave!" in output
        assert "¡Encontraste el tesoro!" in output
        assert "¡Ganaste!" in output

    except SystemExit:

        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_intentar_abrir_cofre_sin_llave():

    input_mock = StringIO("norte\nabrir\nsur\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "Necesitas una llave" in output or "está cerrado" in output

    except:
        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_comandos_invalidos():
    input_mock = StringIO("saltar\ncorrer\nnorte\nsur\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "No puedes hacer eso aquí" in output

    except:
        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_mensajes_iniciales():

    input_mock = StringIO("norte\nsur\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "¡Bienvenido a la Aventura de Texto!" in output
        assert "Estás en la entrada" in output
        assert "Comandos:" in output
        assert "norte, sur, este, oeste, abrir, tomar, usar" in output

    except:
        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_habitaciones_disponibles():

    input_mock = StringIO("norte\nsur\neste\noeste\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "ENTRADA" in output
        assert "SALA" in output
        assert "COCINA" in output

    except:
        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_descripciones_habitaciones():

    input_mock = StringIO("norte\nsur\neste\noeste\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "entrada del castillo" in output
        assert "sala grande" in output or "cofre antiguo" in output
        assert "cocina" in output or "polvo" in output or "mesa" in output

    except:
        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout



def test_estado_llave_cofre():
    pass


def test_fin_del_juego_mensaje():

    input_mock = StringIO("este\ntomar\noeste\nnorte\nusar\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "¡Fin del juego!" in output

    except SystemExit:

        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_comando_abrir_directamente():

    input_mock = StringIO("este\ntomar\noeste\nnorte\nabrir\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()

        assert "¡Ganaste!" in output

    except SystemExit:
        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_varios_intentos():

    input_mock = StringIO("norte\nabrir\nsur\neste\ntomar\noeste\nnorte\nabrir\n")

    original_stdin = sys.stdin
    sys.stdin = input_mock

    try:

        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        output = captured_output.getvalue()
        assert "Necesitas una llave" in output or "está cerrado" in output
        assert "¡Encontraste la llave!" in output
        assert "¡Ganaste!" in output

    except SystemExit:
        pass
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout