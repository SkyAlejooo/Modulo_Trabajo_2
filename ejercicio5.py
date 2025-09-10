def clasificar_numero(numero: int) -> tuple:

    paridad = "Par" if numero % 2 == 0 else "Impar"
    mensaje_extra = "y también es múltiplo de 5" if numero % 5 == 0 else ""

    return paridad, mensaje_extra


def main():

    try:
        numero = int(input("Ingrese un número: "))
        paridad, mensaje_extra = clasificar_numero(numero)

        resultado = f"El número {numero} es {paridad}"
        if mensaje_extra:
            resultado += f" {mensaje_extra}"

        print(resultado)

    except ValueError:
        print("Error: Debe ingresar un número válido.")


if __name__ == "__main__":
    main()