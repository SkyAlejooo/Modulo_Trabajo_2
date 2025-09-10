def combinar_listas(nombres: list, notas: list) -> dict:

    if len(nombres) != len(notas):
        raise ValueError("Las listas deben tener la misma longitud")

    return dict(zip(nombres, notas))


def main():

    nombres = ["Ana", "Luis", "Maria", "Carlos", "Laura"]
    notas = [4.5, 3.8, 4.9, 3.2, 4.7]

    try:
        estudiantes = combinar_listas(nombres, notas)

        print("Reporte de notas:")
        print("-" * 30)
        for nombre, nota in estudiantes.items():
            print(f"El estudiante {nombre} tiene una nota de {nota}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()