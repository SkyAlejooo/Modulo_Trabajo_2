def main():

    habitacion_actual = "entrada"
    llave_encontrada = False
    cofre_abierto = False

    print("¡Bienvenido a la Aventura de Texto!")
    print("Estás en la entrada de un castillo abandonado.")
    print("Comandos: norte, sur, este, oeste, abrir, tomar, usar")

    while True:
        print(f"\n--- Estás en: {habitacion_actual.upper()} ---")

        if habitacion_actual == "entrada":
            print("Estás en la entrada del castillo.")
            print("Hay puertas al norte y este.")
            accion = input("¿Qué haces? ").lower()

            if accion == "norte":
                habitacion_actual = "sala"
            elif accion == "este":
                habitacion_actual = "cocina"
            else:
                print("No puedes hacer eso aquí.")

        elif habitacion_actual == "sala":
            print("Estás en una sala grande con un cofre antiguo.")
            if not cofre_abierto:
                print("El cofre parece estar cerrado con llave.")
            accion = input("¿Qué haces? ").lower()

            if accion == "sur":
                habitacion_actual = "entrada"
            elif accion == "abrir" and not cofre_abierto:
                if llave_encontrada:
                    print("¡Abriste el cofre! Encontraste el tesoro. ¡Ganaste!")
                    break
                else:
                    print("El cofre está cerrado. Necesitas una llave.")
            elif accion == "usar" and llave_encontrada and not cofre_abierto:
                print("Usaste la llave para abrir el cofre. ¡Encontraste el tesoro! ¡Ganaste!")
                break
            else:
                print("No puedes hacer eso aquí.")

        elif habitacion_actual == "cocina":
            print("Estás en la cocina. Hay polvo por todas partes.")
            if not llave_encontrada:
                print("Sobre la mesa hay una llave brillante.")
            accion = input("¿Qué haces? ").lower()

            if accion == "oeste":
                habitacion_actual = "entrada"
            elif accion == "tomar" and not llave_encontrada:
                llave_encontrada = True
                print("¡Encontraste la llave! Ahora puedes abrir el cofre.")
            else:
                print("No puedes hacer eso aquí.")

    print("\n¡Fin del juego!")


if __name__ == "__main__":
    main()