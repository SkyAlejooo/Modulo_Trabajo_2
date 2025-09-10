import pytest
from ejercicio15 import BatallaNaval  # Asegúrate de que el archivo se llame batalla_naval.py


class TestBatallaNaval:


    def test_inicializacion(self):
        juego = BatallaNaval()

        assert juego.tamano == 5
        assert len(juego.tablero) == 5
        assert len(juego.tablero[0]) == 5
        assert all(celda == '~' for fila in juego.tablero for celda in fila)
        assert juego.barco == []
        assert juego.turnos_restantes == 10
        assert juego.barcos_hundidos == 0
        assert juego.coordenadas_disparadas == set()

    def test_colocar_barco_tamano(self):
        juego = BatallaNaval()
        juego.colocar_barco()

        assert len(juego.barco) == 3
        assert all(isinstance(pos, tuple) and len(pos) == 2 for pos in juego.barco)

    def test_colocar_barco_dentro_tablero(self):
        juego = BatallaNaval()
        juego.colocar_barco()

        for fila, columna in juego.barco:
            assert 0 <= fila < juego.tamano
            assert 0 <= columna < juego.tamano

    def test_colocar_barco_posiciones_consecutivas(self):
        juego = BatallaNaval()
        juego.colocar_barco()

        filas = [pos[0] for pos in juego.barco]
        columnas = [pos[1] for pos in juego.barco]

        if len(set(filas)) == 1:  # Horizontal
            assert columnas == sorted(columnas)
            assert columnas[2] - columnas[0] == 2
        else:
            assert len(set(columnas)) == 1
            assert filas == sorted(filas)
            assert filas[2] - filas[0] == 2

    def test_convertir_coordenada_valida(self):
        juego = BatallaNaval()

        test_cases = [
            ('A1', (0, 0)),
            ('B2', (1, 1)),
            ('C3', (2, 2)),
            ('D4', (3, 3)),
            ('E5', (4, 4)),
            ('a1', (0, 0)),
            ('e5', (4, 4))
        ]

        for coordenada, esperado in test_cases:
            resultado = juego.convertir_coordenada(coordenada)
            assert resultado == esperado, f"Falló para {coordenada}"

    def test_convertir_coordenada_invalida(self):
        juego = BatallaNaval()

        test_cases = [
            ('', "Formato inválido"),
            ('A', "Formato inválido"),
            ('1', "Formato inválido"),
            ('A10', "Formato inválido"),
            ('F1', "Coordenada fuera"),
            ('A6', "Coordenada fuera"),
            ('Z1', "Coordenada fuera"),
            ('A0', "Coordenada fuera"),
            ('1A', "Formato inválido"),
            ('AA', "Formato inválido"),
            ('11', "Formato inválido")
        ]

        for coordenada, mensaje_esperado in test_cases:
            with pytest.raises(ValueError) as exc_info:
                juego.convertir_coordenada(coordenada)
            assert mensaje_esperado in str(exc_info.value)

    def test_disparar_agua(self):
        juego = BatallaNaval()
        juego.barco = [(0, 0), (0, 1), (0, 2)]

        resultado = juego.disparar(4, 4)

        assert resultado == "agua"
        assert juego.tablero[4][4] == 'O'
        assert (4, 4) in juego.coordenadas_disparadas
        assert juego.turnos_restantes == 10

    def test_disparar_tocado(self):
        juego = BatallaNaval()
        juego.barco = [(0, 0), (0, 1), (0, 2)]

        resultado = juego.disparar(0, 1)

        assert resultado == "tocado"
        assert juego.tablero[0][1] == 'X'
        assert (0, 1) in juego.coordenadas_disparadas

    def test_disparar_repetido(self):
        juego = BatallaNaval()
        juego.barco = [(0, 0), (0, 1), (0, 2)]
        juego.coordenadas_disparadas.add((1, 1))

        resultado = juego.disparar(1, 1)

        assert resultado == "repetido"
        assert juego.tablero[1][1] == '~'

    def test_disparar_hundido(self):
        juego = BatallaNaval()
        juego.barco = [(0, 0), (0, 1), (0, 2)]

        resultado1 = juego.disparar(0, 0)
        assert resultado1 == "tocado"

        resultado2 = juego.disparar(0, 1)
        assert resultado2 == "tocado"

        resultado3 = juego.disparar(0, 2)
        assert resultado3 == "hundido"

        assert juego.barcos_hundidos == 0

    def test_flujo_completo_victoria(self):
        juego = BatallaNaval()
        juego.barco = [(2, 1), (2, 2), (2, 3)]

        juego.disparar(2, 1)
        juego.disparar(2, 2)
        resultado = juego.disparar(2, 3)

        assert resultado == "hundido"
        assert juego.tablero[2][1] == 'X'
        assert juego.tablero[2][2] == 'X'
        assert juego.tablero[2][3] == 'X'

    def test_flujo_completo_derrota(self):
        juego = BatallaNaval()
        juego.barco = [(0, 0), (0, 1), (0, 2)]

        for i in range(10):
            juego.turnos_restantes -= 1

        assert juego.turnos_restantes == 0
        assert juego.barcos_hundidos == 0


class TestIntegracion:

    def test_juego_completo_victoria(self):
        juego = BatallaNaval()
        juego.barco = [(1, 1), (1, 2), (1, 3)]

        juego.disparar(1, 1)
        juego.disparar(1, 2)
        juego.disparar(1, 3)


        assert all(juego.tablero[1][col] == 'X' for col in [1, 2, 3])
        assert len(juego.coordenadas_disparadas) == 3

    def test_verificacion_barco_valido(self):
        for _ in range(100):
            juego = BatallaNaval()
            juego.colocar_barco()

            assert len(juego.barco) == len(set(juego.barco))

            for fila, columna in juego.barco:
                assert 0 <= fila < juego.tamano
                assert 0 <= columna < juego.tamano


def test_mostrar_tablero_no_falla():
    juego = BatallaNaval()
    juego.colocar_barco()

    try:
        juego.mostrar_tablero()
        assert True
    except Exception:
        pytest.fail("mostrar_tablero() generó una excepción")


def test_colocar_multiples_barcos():
    juego = BatallaNaval()

    barcos = set()
    for _ in range(50):
        juego.colocar_barco()
        barco_tuple = tuple(sorted(juego.barco))
        barcos.add(barco_tuple)

    assert len(barcos) > 1, "El barco siempre se coloca en la misma posición"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])