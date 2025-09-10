def transponer_matriz_bucles(matriz: list) -> list:

    if not matriz:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)

    return transpuesta


def transponer_matriz_comprehension(matriz: list) -> list:

    if not matriz:
        return []

    return [[matriz[i][j] for i in range(len(matriz))]
            for j in range(len(matriz[0]))]


def main():

    matriz = [[1, 2, 3], [4, 5, 6]]

    print("Matriz original:")
    for fila in matriz:
        print(fila)

    print("\nTranspuesta (bucles):")
    transpuesta_bucles = transponer_matriz_bucles(matriz)
    for fila in transpuesta_bucles:
        print(fila)

    print("\nTranspuesta (comprehension):")
    transpuesta_comp = transponer_matriz_comprehension(matriz)
    for fila in transpuesta_comp:
        print(fila)


if __name__ == "__main__":
    main()