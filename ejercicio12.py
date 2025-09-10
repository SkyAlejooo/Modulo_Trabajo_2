import random
from collections import defaultdict


def simular_lanzamientos(cantidad: int = 10000) -> dict:

    frecuencias = defaultdict(int)

    for _ in range(cantidad):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        frecuencias[suma] += 1

    return dict(frecuencias)


def main():

    print("Simulador de Lanzamiento de Dados")
    print("Simulando 10,000 lanzamientos...")

    frecuencias = simular_lanzamientos()

    print("\nResultados:")
    print("Suma | Frecuencia | Porcentaje")
    print("-" * 30)

    for suma in range(2, 13):
        frecuencia = frecuencias.get(suma, 0)
        porcentaje = (frecuencia / 10000) * 100
        print(f"{suma:4} | {frecuencia:9} | {porcentaje:8.2f}%")


if __name__ == "__main__":
    main()