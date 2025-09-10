def encontrar_indices(frase: str, letra: str) -> list:

    indices = []
    for i, caracter in enumerate(frase):
        if caracter.lower() == letra.lower():
            indices.append(i)
    return indices


def main():

    frase = input("Ingrese una frase: ")
    letra = input("Ingrese la letra a buscar: ")

    indices = encontrar_indices(frase, letra)
    print(f"La letra '{letra}' aparece en las posiciones: {indices}")


if __name__ == "__main__":
    main()