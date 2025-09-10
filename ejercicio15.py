import random


class BatallaNaval:


    def __init__(self):
        self.tamano = 5
        self.tablero = [['~' for _ in range(self.tamano)] for _ in range(self.tamano)]
        self.barco = []
        self.turnos_restantes = 10
        self.barcos_hundidos = 0
        self.coordenadas_disparadas = set()

    def colocar_barco(self):

        orientacion = random.choice(['horizontal', 'vertical'])

        if orientacion == 'horizontal':
            fila = random.randint(0, self.tamano - 1)
            columna = random.randint(0, self.tamano - 3)
            self.barco = [(fila, columna + i) for i in range(3)]
        else:
            fila = random.randint(0, self.tamano - 3)
            columna = random.randint(0, self.tamano - 1)
            self.barco = [(fila + i, columna) for i in range(3)]

    def mostrar_tablero(self):

        print("  A B C D E")
        for i in range(self.tamano):
            print(f"{i + 1} ", end="")
            for j in range(self.tamano):
                print(self.tablero[i][j], end=" ")
            print()

    def convertir_coordenada(self, coordenada):

        if len(coordenada) != 2 or not coordenada[0].isalpha() or not coordenada[1].isdigit():
            raise ValueError("Formato inválido. Use letra+número (ej. A1)")

        columna = ord(coordenada[0].upper()) - ord('A')
        fila = int(coordenada[1]) - 1

        if not (0 <= fila < self.tamano and 0 <= columna < self.tamano):
            raise ValueError("Coordenada fuera del tablero")

        return fila, columna

    def disparar(self, fila, columna):

        if (fila, columna) in self.coordenadas_disparadas:
            return "repetido"

        self.coordenadas_disparadas.add((fila, columna))

        if (fila, columna) in self.barco:
            self.tablero[fila][columna] = 'X'

            if all((f, c) in self.coordenadas_disparadas for f, c in self.barco):
                return "hundido"
            return "tocado"
        else:
            self.tablero[fila][columna] = 'O'
            return "agua"

    def jugar(self):

        self.colocar_barco()
        print("¡Bienvenido a Batalla Naval!")
        print("Tienes 10 turnos para hundir el barco de 3 casillas.")
        print("Coordenadas: A1 hasta E5")

        while self.turnos_restantes > 0 and self.barcos_hundidos == 0:
            print(f"\nTurnos restantes: {self.turnos_restantes}")
            self.mostrar_tablero()

            while True:
                try:
                    coordenada = input("Ingresa coordenada (ej. A1): ").strip().upper()
                    fila, columna = self.convertir_coordenada(coordenada)
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            resultado = self.disparar(fila, columna)

            if resultado == "repetido":
                print("Ya disparaste aquí. Pierdes turno.")
                self.turnos_restantes -= 1
            elif resultado == "tocado":
                print("¡Tocado!")
                self.turnos_restantes -= 1
            elif resultado == "hundido":
                print("¡Barco hundido! ¡Ganaste!")
                self.barcos_hundidos = 1
            else:
                print("Agua.")
                self.turnos_restantes -= 1

        print("\nTablero final:")
        self.mostrar_tablero()

        if self.barcos_hundidos == 1:
            print("¡Felicidades! Ganaste el juego.")
        else:
            print("¡Perdiste! Se acabaron los turnos.")
            print("El barco estaba en:", self.barco)


def main():

    juego = BatallaNaval()
    juego.jugar()


if __name__ == "__main__":
    main()