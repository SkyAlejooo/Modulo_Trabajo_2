import pytest
from ejercicio3 import validar_contraseña


class TestValidarContraseña:

    def test_contraseña_valida(self):
        resultado = validar_contraseña("Password123")
        assert resultado == []

    def test_contraseña_corta(self):
        resultado = validar_contraseña("Pass1")
        assert "Mínimo 8 caracteres" in resultado
        assert len(resultado) == 1

    def test_sin_mayuscula(self):
        resultado = validar_contraseña("password123")
        assert "Al menos una letra mayúscula" in resultado
        assert len(resultado) == 1

    def test_sin_numero(self):
        resultado = validar_contraseña("Password")
        assert "Al menos un número" in resultado
        assert len(resultado) == 1

    def test_multiples_errores(self):
        resultado = validar_contraseña("pass")
        assert len(resultado) == 3
        assert "Mínimo 8 caracteres" in resultado
        assert "Al menos una letra mayúscula" in resultado
        assert "Al menos un número" in resultado

    def test_contraseña_vacia(self):
        resultado = validar_contraseña("")
        assert len(resultado) == 3
        assert "Mínimo 8 caracteres" in resultado
        assert "Al menos una letra mayúscula" in resultado
        assert "Al menos un número" in resultado

    def test_solo_numeros(self):
        resultado = validar_contraseña("12345678")
        assert len(resultado) == 1
        assert "Al menos una letra mayúscula" in resultado
        assert "Mínimo 8 caracteres" not in resultado

    def test_solo_mayusculas(self):

        resultado = validar_contraseña("PASSWORD")
        assert len(resultado) == 1
        assert "Al menos un número" in resultado
        assert "Mínimo 8 caracteres" not in resultado

    def test_caracteres_especiales_validos(self):
        resultado = validar_contraseña("Pass@1234")
        assert resultado == []

    def test_longitud_exacta_8(self):
        resultado = validar_contraseña("Pass1234")
        assert resultado == []

    def test_primera_letra_mayuscula(self):
        resultado = validar_contraseña("Password123")
        assert resultado == []

    def test_ultimo_caracter_numero(self):
        resultado = validar_contraseña("password1A")
        assert resultado == []


@pytest.mark.parametrize("contraseña,errores_esperados", [
    ("A1" + "a" * 6, []),
    ("a" * 7, ["Mínimo 8 caracteres", "Al menos una letra mayúscula", "Al menos un número"]),
    ("A" * 8, ["Al menos un número"]),
    ("1" * 8, ["Al menos una letra mayúscula"]),
    ("Aa1", ["Mínimo 8 caracteres"]),
    ("AAAAAAAA1", []),
    ("aaaaaaaa1", ["Al menos una letra mayúscula"]),
    ("AAAAAAAa", ["Al menos un número"]),
])
def test_validar_contraseña_parametrizado(contraseña, errores_esperados):
    resultado = validar_contraseña(contraseña)
    assert len(resultado) == len(errores_esperados)
    for error in errores_esperados:
        assert error in resultado