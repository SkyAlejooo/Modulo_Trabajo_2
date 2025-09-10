import random


class Ahorcado:
    def __init__(self):

        self.palabras = ["python", "programacion", "computadora", "algoritmo", "desarrollo"]
        self.palabra_secreta = ""
        self.letras_adivinadas = set()
        self.letras_intentadas = set()
        self.vidas = 6
        self.ganado = False

    def seleccionar_palabra(self):

        self.palabra_secreta = random.choice(self.palabras)
        return self.palabra_secreta

    def mostrar_tablero(self):

        tablero = []
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                tablero.append(letra)
            else:
                tablero.append("_")


        print("Palabra: " + " ".join(tablero))
        print(f"Vidas restantes: {self.vidas}")


        if self.letras_intentadas:
            letras_ordenadas = sorted(self.letras_intentadas)
            print(f"Letras intentadas: {', '.join(letras_ordenadas)}")

    def procesar_intento(self, letra):

        letra = letra.lower()


        if letra in self.letras_intentadas:
            return


        self.letras_intentadas.add(letra)


        if letra in self.palabra_secreta:
            self.letras_adivinadas.add(letra)


            if all(letra in self.letras_adivinadas for letra in self.palabra_secreta):
                self.ganado = True
        else:

            if self.vidas > 0:
                self.vidas -= 1

    def jugar(self):

        self.seleccionar_palabra()


        print("¡Bienvenido al Ahorcado!")
        print("Adivina la palabra secreta.")


        while self.vidas > 0 and not self.ganado:
            print("\n" + "=" * 40)
            self.mostrar_tablero()


            while True:
                intento = input("Ingresa una letra: ").strip()

                if len(intento) != 1:
                    print("Por favor, ingresa una sola letra.")
                    continue

                if not intento.isalpha():
                    print("Por favor, ingresa solo letras.")
                    continue

                intento = intento.lower()

                if intento in self.letras_intentadas:
                    print("Ya intentaste esa letra.")
                    continue

                break


            self.procesar_intento(intento)


        print("\n" + "=" * 40)
        if self.ganado:
            print(f"¡Felicidades! Ganaste. La palabra era: {self.palabra_secreta}")
        else:
            print(f"¡Perdiste! La palabra era: {self.palabra_secreta}")


def main():

    juego = Ahorcado()
    juego.jugar()


if __name__ == "__main__":

    main()