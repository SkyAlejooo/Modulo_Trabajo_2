import pytest
from ejercicio14 import Ahorcado


class TestAhorcado:


    def test_inicializacion(self):

        juego = Ahorcado()

        assert juego.palabras == ["python", "programacion", "computadora", "algoritmo", "desarrollo"]
        assert juego.palabra_secreta == ""
        assert juego.letras_adivinadas == set()
        assert juego.letras_intentadas == set()
        assert juego.vidas == 6
        assert juego.ganado is False

    def test_seleccionar_palabra_valida(self):

        juego = Ahorcado()
        palabra_seleccionada = juego.seleccionar_palabra()

        assert palabra_seleccionada in juego.palabras
        assert juego.palabra_secreta == palabra_seleccionada
        assert isinstance(palabra_seleccionada, str)
        assert len(palabra_seleccionada) > 0

    def test_procesar_intento_letra_correcta(self):

        juego = Ahorcado()
        juego.palabra_secreta = "python"
        juego.letras_intentadas = set()
        juego.letras_adivinadas = set()

        juego.procesar_intento('p')

        assert 'p' in juego.letras_intentadas
        assert 'p' in juego.letras_adivinadas
        assert juego.vidas == 6
        assert juego.ganado is False

    def test_procesar_intento_letra_incorrecta(self):

        juego = Ahorcado()
        juego.palabra_secreta = "python"
        juego.letras_intentadas = set()
        juego.letras_adivinadas = set()
        vidas_iniciales = juego.vidas

        juego.procesar_intento('z')

        assert 'z' in juego.letras_intentadas
        assert 'z' not in juego.letras_adivinadas
        assert juego.vidas == vidas_iniciales - 1
        assert juego.ganado is False

    def test_procesar_intento_letra_repetida(self):

        juego = Ahorcado()
        juego.palabra_secreta = "python"
        juego.letras_intentadas = {'p'}
        juego.letras_adivinadas = {'p'}
        vidas_iniciales = juego.vidas


        juego.procesar_intento('p')

        assert juego.letras_intentadas == {'p'}
        assert juego.letras_adivinadas == {'p'}
        assert juego.vidas == vidas_iniciales

    def test_procesar_intento_case_insensitive(self):
        juego = Ahorcado()
        juego.palabra_secreta = "python"
        juego.letras_intentadas = set()
        juego.letras_adivinadas = set()

        juego.procesar_intento('P')
        juego.procesar_intento('y')

        assert 'p' in juego.letras_intentadas
        assert 'y' in juego.letras_intentadas
        assert 'p' in juego.letras_adivinadas
        assert 'y' in juego.letras_adivinadas

    def test_victoria_completa(self):

        juego = Ahorcado()
        juego.palabra_secreta = "sol"
        juego.letras_intentadas = set()
        juego.letras_adivinadas = set()


        juego.procesar_intento('s')
        assert juego.ganado is False

        juego.procesar_intento('o')
        assert juego.ganado is False

        juego.procesar_intento('l')
        assert juego.ganado is True
        assert juego.vidas == 6

    def test_derrota_por_vidas(self):
        juego = Ahorcado()
        juego.palabra_secreta = "sol"
        juego.letras_intentadas = set()
        juego.letras_adivinadas = set()

        # Verificar vidas iniciales
        assert juego.vidas == 6

        letras_incorrectas = ['x', 'y', 'z', 'w', 'q', 'p']

        for letra in letras_incorrectas:
            juego.procesar_intento(letra)

        assert juego.vidas == 0, f"Expected 0 vidas, but got {juego.vidas}"
        assert juego.ganado is False
        assert len(juego.letras_intentadas) == 6
        assert len(juego.letras_adivinadas) == 0

    def test_mostrar_tablero_palabra_oculta(self):

        juego = Ahorcado()
        juego.palabra_secreta = "python"
        juego.letras_intentadas = set()
        juego.letras_adivinadas = set()


        tablero_esperado = ['_', '_', '_', '_', '_', '_']


        tablero_real = []
        for letra in juego.palabra_secreta:
            if letra in juego.letras_adivinadas:
                tablero_real.append(letra)
            else:
                tablero_real.append('_')

        assert tablero_real == tablero_esperado

    def test_mostrar_tablero_palabra_parcial(self):

        juego = Ahorcado()
        juego.palabra_secreta = "python"
        juego.letras_intentadas = {'p', 'y'}
        juego.letras_adivinadas = {'p', 'y'}

        tablero_esperado = ['p', 'y', '_', '_', '_', '_']

        tablero_real = []
        for letra in juego.palabra_secreta:
            if letra in juego.letras_adivinadas:
                tablero_real.append(letra)
            else:
                tablero_real.append('_')

        assert tablero_real == tablero_esperado

    def test_mostrar_tablero_palabra_completa(self):

        juego = Ahorcado()
        juego.palabra_secreta = "sol"
        juego.letras_intentadas = {'s', 'o', 'l'}
        juego.letras_adivinadas = {'s', 'o', 'l'}

        tablero_esperado = ['s', 'o', 'l']

        tablero_real = []
        for letra in juego.palabra_secreta:
            if letra in juego.letras_adivinadas:
                tablero_real.append(letra)
            else:
                tablero_real.append('_')

        assert tablero_real == tablero_esperado


def test_orden_letras_intentadas():

    juego = Ahorcado()
    juego.letras_intentadas = {'z', 'a', 'm'}


    letras_ordenadas = sorted(juego.letras_intentadas)
    assert letras_ordenadas == ['a', 'm', 'z']



def test_flujo_completo_victoria():

    juego = Ahorcado()
    juego.palabra_secreta = "casa"


    juego.procesar_intento('c')
    juego.procesar_intento('a')
    juego.procesar_intento('s')

    assert juego.ganado is True
    assert juego.vidas == 6
    assert juego.letras_adivinadas == {'c', 'a', 's'}


def test_flujo_completo_derrota():

    juego = Ahorcado()
    juego.palabra_secreta = "casa"


    for letra in ['x', 'y', 'z', 'w', 'q', 'p']:
        juego.procesar_intento(letra)

    assert juego.vidas == 0
    assert juego.ganado is False
    assert len(juego.letras_adivinadas) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])