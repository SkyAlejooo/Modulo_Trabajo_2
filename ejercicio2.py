def procesar_comando(comando):

    comando = comando.lower().strip()

    if comando == "guardar":
        return "Guardando archivo..."
    elif comando == "cargar":
        return "Cargando archivo..."
    elif comando == "salir":
        return None
    else:
        return "Error: Comando no válido. Intente nuevamente."


def main():

    print("Bienvenido al Intérprete de Comandos")
    print("Comandos disponibles: guardar, cargar, salir")

    while True:
        entrada_usuario = input("\nIngrese comando: ")
        resultado = procesar_comando(entrada_usuario)

        if resultado is None:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print(resultado)


if __name__ == "__main__":
    main()