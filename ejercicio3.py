def validar_contraseña(contraseña: str) -> list:
    errores = []

    if len(contraseña) < 8:
        errores.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in contraseña):
        errores.append("Al menos una letra mayúscula")
    if not any(c.isdigit() for c in contraseña):
        errores.append("Al menos un número")

    return errores


def main():

    print("Cree una contraseña que cumpla con:")
    print("- Mínimo 8 caracteres")
    print("- Al menos una letra mayúscula")
    print("- Al menos un número")

    while True:
        contraseña = input("\nIngrese su contraseña: ")
        errores = validar_contraseña(contraseña)

        if not errores:
            print("¡Contraseña válida!")
            break

        print("Errores encontrados:")
        for error in errores:
            print(f"- {error}")
        print("Intente nuevamente.")


if __name__ == "__main__":
    main()