def validar_cedula(cedula: str) -> bool:

    if not cedula.isdigit():
        return False

    suma = sum(int(digito) for digito in cedula)
    return suma % 2 == 0


def main():

    print("Validador de Cédula")
    print("La suma de los dígitos debe ser par")

    while True:
        cedula = input("\nIngrese su cédula (solo números): ").strip()

        if validar_cedula(cedula):
            print("¡Cédula válida!")
            break
        else:
            print("Cédula no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()