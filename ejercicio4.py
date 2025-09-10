import random

def determinar_ganador(jugador: str, computadora: str) -> str:
    if jugador == computadora:
        return 'empate'

    if (jugador == 'piedra' and computadora == 'tijeras') or \
            (jugador == 'tijeras' and computadora == 'papel') or \
            (jugador == 'papel' and computadora == 'piedra'):
        return 'jugador'
    else:
        return 'computadora'


def main():
    opciones = ['piedra', 'papel', 'tijeras']
    victorias_jugador = 0
    victorias_computadora = 0

    print("¡Piedra, Papel o Tijeras!")
    print("Gana el primero en llegar a 3 victorias")

    while victorias_jugador < 3 and victorias_computadora < 3:
        print(f"\nMarcador: Jugador {victorias_jugador} - {victorias_computadora} Computadora")

        jugador = input("Elige (piedra/papel/tijeras): ").lower()
        if jugador not in opciones:
            print("Opción no válida. Intenta nuevamente.")
            continue

        computadora = random.choice(opciones)
        print(f"Computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)

        if resultado == 'jugador':
            victorias_jugador += 1
            print("¡Ganaste esta ronda!")
        elif resultado == 'computadora':
            victorias_computadora += 1
            print("La computadora gana esta ronda.")
        else:
            print("Empate.")

    if victorias_jugador == 3:
        print("\n¡Felicidades! Ganaste el juego.")
    else:
        print("\nLa computadora gana el juego.")


if __name__ == "__main__":
    main()